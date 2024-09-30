"""
Given a weighted adjacency list, our task is to identify the sum of the MST in the graph

PRIMS ALGORITHM :
    - Greedy algorithm that expands the MST by selecting the smallest weight edge from the current tree to a new vertex.
    •  Visited ARRAY to track the nodes
    •   Initialize a priority queue (min-heap) to store edges with weights.
        -> PQ holds (wt,node,parent) Min heap is formed based on the weight.
	•	Start from any node and add its edges to the heap.
	•	While the heap is not empty, pick the edge with the smallest weight.
	•	If the node is not yet visited, mark it as visited and add its adjacent edges to the heap.
	•	Continue until all nodes are visited.
KEY POINTS:
    Mark node as visited only after we add it to the sum /mst list.

"""

from typing import List
import heapq

class Solution:

    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        visited = [0]*len(adj)
        pq = [(0,0,-1)]
        sum = 0
        #mst = []
        while pq:
            wt,node,root = heapq.heappop(pq)
            if visited[node]:
                continue

            sum+=wt
            #mst.append([node,root])
            visited[node] = 1

            for neighbor,wt in adj[node]:
                if visited[neighbor]==0:
                    heapq.heappush(pq,(wt,neighbor,node))
        return sum #, mst
