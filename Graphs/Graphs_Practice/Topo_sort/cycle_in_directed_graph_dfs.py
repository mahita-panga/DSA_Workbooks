"""
GFG: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Intuition:
    -> Using DFS for traversing depth wise. (BFS needs topo sort learning--Not yet reached there)
    -> We maintain 2 arrays: visited and path visited
        visited: To track visited status of all the vertices
        path_visited : To track the vertices being visited in the current path
    -> For all nodes in adj_list:
        if node is not visited:
            dfs(current_node), if cycle found anywhere propogate true else return false
        return False

        dfs(node,adj_list,visited,path_visited):
            visited[node] =1 //marking node as visited
            path_visited[node] = 1 //marking node as visited in curr_path as well

            for all neighbours of node in adj list:
                if visited[neighbour] == 0:
                    if dfs(neighbour):
                        return True //propogating the status if cycle is found
                elif path_visited[neighbour] == 1:
                    return True //CYCLE FOUND
            path_visited[node] = 0 //no cycle, setting it 0 during backtracking
            return False //no cycle found as of now.

"""
#User function Template for python3
from typing import List

class Solution:

    def dfs(self,curr_node,adj,visited,path_visited):
        visited[curr_node] = 1
        path_visited[curr_node] = 1

        for i in adj[curr_node]:
            if visited[i] == 0:
                if self.dfs(i,adj,visited,path_visited):
                    return True
            elif path_visited[i] == 1:
                return True
        path_visited[curr_node] = 0
        return False



    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        visited = [0] * V
        path_visited = [0] * V

        for i in range(len(adj)):
            if visited[i] == 0:
                if self.dfs(i,adj,visited,path_visited):
                    return True
        return False

"""
Time Complexity: O(V)+O(V+E)(dfs traversal) ~ O(V+E)
Space Complexity: O(V)(visited) + O(V)(path_visited) + O(V)(rec stack) ~ O(V)
"""
