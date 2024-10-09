from typing import List

"""
Logic: DSU on Sorted weight edges
- DSU -> add_edge -> return True if edge was added, False if not added (u->v was already added and had same super parent)
- Sort edges based on weights and then add_edge for each, if added -> add wt to result
- This way you never add same edge again to a region (you need min edge between 2 edges which you already got since you sorted by weigth)

"""

class Disjoint_Set:
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.size = [1] * (N+1)

    def get_parent(self):
        return self.parent

    def findUP(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUP(self.parent[node])  # Path compression
        return self.parent[node]

    # Union by Size
    def UnionBySize(self, u, v):
        pu = self.findUP(u)
        pv = self.findUP(v)

        if pu != pv:  # They are in different sets
            # Attach the smaller tree under the larger tree
            if self.size[pu] < self.size[pv]:
                self.parent[pu] = pv  # Attach u's root to v's root
                self.size[pv] += self.size[pu]  # Update size of v's root
            else:
                self.parent[pv] = pu  # Attach v's root to u's root
                self.size[pu] += self.size[pv]  # Update size of u's root


def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # sort acc to weights since you need Minimum Spanning Tree
    edges = sorted(edges, key=lambda x:x[2]) #sort edges based on weights

    total_wt = 0
    dsu = Disjoint_Set(n)

    for u,v,wt in edges:
        if dsu.UnionBySize(u,v): # this node is already added -> will cause cycle/its already reachable
            total_wt += wt

    return total_wt
