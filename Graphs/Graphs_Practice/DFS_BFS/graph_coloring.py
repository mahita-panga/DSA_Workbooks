"""
LC #785. Is Graph Bipartite?
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Intuition:
    -> We can do BFS/DFS traversal over graph to color it.
    -> We consider coloring array = [-1] * V  -1 indicates it has not been colored yet
    -> I consider 2 colors 0 and 1.
    -> For all nodes in graph:
        if coloring is -1:
            then color curr node with 0.
            add it to q
            do BFS, while doing BFS,
            check if the neighbour_node's color is -1 , then color it with opposite color of neighbour node.
            if color of neighbour_node == color of curr node then it means there is a cycle and bipartite graph
            is not possible. Then return False
        return True //all nodes are colored.

"""
from collections import deque
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coloring = [-1]*len(graph)
        for i in range(len(graph)):
            if coloring[i] == -1:
                q = deque([i])
                coloring[i] = 0

            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if coloring[neighbor] == -1:
                        coloring[neighbor] = 1 - coloring[node]  # Assign opposite color
                        q.append(neighbor)
                    elif coloring[neighbor] == coloring[node]:
                        return False
        return True
