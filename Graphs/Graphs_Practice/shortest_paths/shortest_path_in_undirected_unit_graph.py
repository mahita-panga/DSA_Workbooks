"""
https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1

Given an undirected graph with unit edges, find the shortest path from  src to all nodes and if no connection between src to
the node, then return -1 in that place.

NOTE : - DFS gave TLE.
       - TOPOSORT should NOT be applied here as it is undirected graph

INTUITION:
    -> Graph Creation:
        With given edges, create an adjancency list. Since it is undirected, add edge to both src and dest adj lists.
    -> Variable initialization:
        -> distance[] -> all initialized to ∞
        P.S: Visited[] is not needed since we need not track the visited status of the graph.
        -> q for bfs traversal
    -> Action:
        -> distance[src] = 0
        -> add src to queue
        -> while queue:
            curr_node = queue.pop()
            if distance[curr] + 1 < distance[neighbour]:
                update distance[neighbour] to distance[curr] + 1 // +1 since it is unit distance
                queue.append(neighbour)
        -> This will ensure shortest path from src to all connected components.
        -> For unconnected components, set dist to -1.


"""

from collections import defaultdict,deque

class Solution:

    # def dfs(self, node, adj, visited, distance):
    #     visited[node] = True
    #     for neighbor in adj[node]:
    #         if not visited[neighbor]:
    #             distance[neighbor] = min(distance[neighbor], distance[node] + 1)
    #             self.dfs(neighbor, adj, visited, distance)
    #         else:
    #             if distance[node] + 1 < distance[neighbor]:
    #                 distance[neighbor] = distance[node] + 1
    #                 self.dfs(neighbor, adj, visited, distance)

    def shortestPath(self, edges, n, m, src):
        # code here
        distance = [float('inf')] * n
        adj = defaultdict(list)

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        q = deque([src])
        distance[src] =0
        while len(q)!= 0 :
            curr = q.popleft()
            for neighbours in adj[curr]:
                if distance[curr]+1 < distance[neighbours]:
                    distance[neighbours] = distance[curr]+1
                    q.append(neighbours)


        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1
        return distance

edges = [
    [0, 1],
    [0, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [1, 2],
    [2, 6],
    [6, 7],
    [7, 8],
    [6, 8]
]
n = 9  # Number of nodes
m = 10  # Number of edges
src = 0
solution = Solution().shortestPath(edges,n,m,src)
