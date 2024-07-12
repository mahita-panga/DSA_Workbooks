"""
Given a DAG, find the shortest path: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/0

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex,
then return -1 for that vertex.

Intuition:
    -> Solved with Toposort and DFS
    -> Graph creation:
        -> create adj list using edges and add weights in the pairs for the adj list

    -> Traversal:
        -> Get the topo sort of the weighted dag( for topo sort, dont consider the weights)
        -> Can use bfs topo sort as well

    -> Distance calculation:
        -> Take a distance array ( all set to infinite values)
        -> set distance[source] = 0 <- since distance to travel to source is 0
        -> in topo order:
            for each neighbour of currnode from adj list:
                check if distance[curr_node]+ weight of this neighbour < distance[neighbour_node]:
                    if true: update distance with distance[curr_node]+ weight
        -> if distance is still infinite, which mean no path exists, update those to -1
        ->return distance
"""

from typing import List
from collections import defaultdict

class Solution:
    def dfs(self,curr,stack,visited,adj):
        visited[curr] = 1
        for neighbour in adj[curr]:
            node = neighbour[0]
            weight = neighbour[1]
            if visited[node] == 0:
                self.dfs(node,stack,visited,adj)
        stack.append(curr)

    def shortestPathDFS(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        visited = [0] * n
        st = [] #stack
        adj = defaultdict(list)
        for i in range(m):
            adj[edges[i][0]].append([edges[i][1],edges[i][2]])

        for i in range(n):
            if visited[i] ==0:
                self.dfs(i,st,visited,adj)

        distance = [float('inf')] * n
        distance[0] = 0
        for i in range(len(st)):
            node = st.pop()
            for neighbour in adj[node]:
                i = neighbour[0]
                wt = neighbour[1]
                if distance[node] + wt < distance[i]:
                    distance[i] = distance[node] + wt
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1

        return distance

    def shortestPathBFS(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        visited = [0] * n
        indegree = [0] * n
        st = [] #stack
        adj = defaultdict(list)
        for i in range(m):
            adj[edges[i][0]].append([edges[i][1],edges[i][2]])
            indegree[edges[i][1]] += 1

        q = deque([x for x in indegree if indegree[x] == 0])

        topo_order = []
        while len(q):
            node = q.popleft()
            visited[node] = 1
            topo_order.append(node)
            for neighbour in adj[node]:
                nnode = neighbour[0]
                weight = neighbour[1]
                if visited[nnode] == 0:
                    indegree[nnode] -= 1
                    if indegree[nnode] == 0:
                        q.append(nnode)


        distance = [float('inf')] * n
        distance[0] = 0
        for i in range(len(topo_order)):
            node = topo_order[i]
            for neighbour in adj[node]:
                i = neighbour[0]
                wt = neighbour[1]
                if distance[node] + wt < distance[i]:
                    distance[i] = distance[node] + wt
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1
        return distance

edges = [
    [0, 1, 2],
    [0, 4, 1],
    [1, 2, 3],
    [4, 2, 2],
    [4, 3, 1],
    [3, 2, 1]
]
n = 5  # Number of nodes
m = 6  # Number of edges

solution = Solution()
result = solution.shortestPathDFS(n, m, edges)
print(result)  # Expected output: [0, 2, 3, 2, 1]
result = solution.shortestPathBFS(n, m, edges)
print(result)
