"""
GFG: https://www.geeksforgeeks.org/problems/eventual-safe-states/1
A directed graph of V vertices and E edges is given in the form of an adjacency list adj. Each node of the graph is labelled with a distinct integer in the range 0 to V - 1.

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

You have to return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Intuition:
    -> All nodes which are not part of cycle are safe nodes.
    -> Similar to Finding Cycle In Directed Graph except that:
        -> We dont break it if cycle is found.
        -> In case we have path_visited and cycle is not found, we need to mark them safe.
        -> Once all the nodes are visited, then fetch the nodes which are all marked safe
        -> This is our result.

    -> Since, we are running it in order of vertices, it would be always be in ascending order.
"""
from typing import List

class Solution:
    def dfs_traversal(self,curr_node,adj,visited,path_visited):
        visited[curr_node] = 1
        path_visited[curr_node] = 1
        for i in adj[curr_node]:
            if visited[i] == 0:
                if self.dfs_traversal(i,adj,visited,path_visited):
                    return True
            elif visited[i] == path_visited[i]:
                return True
        path_visited[curr_node] = 2
        return False

    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        visited = [0] * V
        path_visited = [0] * V
        safe_nodes = []
        for i in range(V):
            if visited[i] == 0:
                self.dfs_traversal(i,adj,visited,path_visited)

        for i in range(V):
            if path_visited[i] == 2:
                safe_nodes.append(i)

        return safe_nodes


V = 7
adj = [[],[0,2],[1,3],[0],[5],[],[2]]
Solution().eventualSafeNodes(V,adj)
