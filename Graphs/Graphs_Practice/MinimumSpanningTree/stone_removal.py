"""
Problem:
- On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
- A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones kept (List<x,y>) return the largest possible number of stones that can be removed.

Intuition:
	•	Stones are connected if they share the same row or column.
	•	The idea is to group stones that are connected (same row or same column) into components. Stones within the same component can be removed except for one stone.
	•	We use Union-Find (Disjoint Set) to track connected components and then calculate the number of moves (removal of stones) as:
ANS: Total stones - Number of connected components.

Union Operation:
	•	For each stone at position (x, y), treat the row x and the column y as nodes and perform a union between them.
	•	To avoid collision between rows and columns (both represented as nodes), we offset the column index by adding a large value (e.g., 10000).
Find Operation (Path Compression):
	•	Use path compression to optimize the find operation, ensuring that we efficiently find the root parent of a node.
Count Components:
	•	After processing all stones, count the number of unique connected components (parents) using the find operation.
Answer:
	•	The result is the number of stones minus the number of components, i.e., len(stones) - number_of_components.

Key Points for Solution:

	1.	Disjoint Set Data Structure:
	•	find(node): Find the ultimate parent (with path compression).
	•	union(u, v): Connect nodes u and v based on the size of their respective components.
	2.	Row-Column Mapping:
	•	Union stones based on their row and column indices, but make sure to differentiate rows from columns by adding an offset (like v+10000+1).
	3.	Connected Components Calculation:
	•	After all union operations, find the number of unique parents for the stones to determine the number of connected components.

Time Complexity:

	•	O(N * α(N)), where N is the number of stones, and α(N) is the inverse Ackermann function, which grows very slowly.

"""
class DisjointSet:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1]*N

    def find(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def get_parent(self):
        return self.parent
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            if self.size[pu] < self.size[pv]:
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]
            else:
                self.parent[pv] = pu
                self.size[pu] += self.size[pv]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        m = len(stones)
        n = len(stones[0])

        maxr = float('-inf')
        maxc = float('-inf')
        for i in range(m):
            maxr = max(maxr,stones[i][0])
            maxc = max(maxc,stones[i][1])

        ds = DisjointSet(200002)
        map = {}
        for u,v in stones:
            ds.union(u,v+10000+1)
            map[u]=1
            map[v]=1
        parent = ds.get_parent()
        nc = len(set(ds.find(x) for x, y in stones))
        return (len(stones) - nc)
