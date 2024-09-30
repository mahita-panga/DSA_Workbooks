"""
LC: 1319. Number of Operations to Make Network Connected

Intuition:
    Consider the computer network like a graph. Now, our objective is to identify the
    -> No.of operations to make network connected
    -> These connections should be fetched from the existing graph.

    To identify the connectivity of graph, we can use Disjoint set data structure.
NOTE: Min. Number of connection to make n disconnected components connected is n-1

    Our steps
    -> Find all extra edges we have i.e. for any edge, if both the edges ultimate parent is same
    then they are already connected and can be counted as extra.
    -> Find all disconnected component, i.e. in parent[] number of nodes that are connected to itself are
   number of disconnected components
  Using above  info, we can identify the number of possible min operations.

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

from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = Disjoint_Set(n)
        extras = 0
        for u,v in connections:
            if ds.findUP(u) == ds.findUP(v): #They are already connected
                extras+=1
            else:
                ds.UnionBySize(u,v)

        parent = ds.get_parent()
        dc = 0
        for i in range(len(parent)):
            if parent[i]==i:
                dc+=1

        if extras >= dc-1:
            return dc-1
        return -1
