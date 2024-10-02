"""
827. Making A Large Island
You are given an n x n binary matrix grid.
You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

-> Break this problem into subproblems:
    -> Create islands from the given grid.
    -> Try to convert any of the 0's to 1 and see if this is helping us create maximum size island
        -> This is done by:
            For all 0's, we will see the adj cells and in case of 1 which means it is part of any particular island,
            we will fetch the size of the island and increment it by 1, and check if it is max.

NOTE: Since we have to maintain information about connected components , we will do UNION FIND.
            Here unionbysize is extremely helpful, which will help us find the size of the island.

            create a component_map to maintain all the neighbouring island groups. Make it set to ensure we dont
            calc same island group twice.
            For any 0 in grid:

            -> Check if any 1 present in all 4 directions
                # this node connects all separate islands in 4 directions together
                add the ultimate parent of this island to component_map

            for all islands in component_map, get total_size and check if this total_size+1 (potential sise after converting 0 to 1)
            Return the max value.

"""
from typing import List
class DSU:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1]*(N)

    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            if self.size[pu]<self.size[pv]:
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]
            else:
                self.parent[pv] = pu
                self.size[pu] += self.size[pv]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ds = DSU(m*n)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        #STEP 1: CONNECT ALL ISLANDS
        for x in range(m):
            for y in range(n):
                if grid[x][y]==1:
                    for dx,dy in directions:
                        nx = x+dx
                        ny = y+dy
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                            node_num = x*n+y
                            new_node_num = nx*n+ny
                            if ds.find(node_num)!=ds.find(new_node_num):
                                ds.union(node_num,new_node_num)


        #STEP 2: CHECK IF ANY NON ISLAND NODES CAN BE CONVERTED
        max_islands = max(ds.size) #Currently set to max size of island possible before transforming any 0's'
        for x in range(m):
            for y in range(n):
                connected_components = set()
                total_size = 0

                if grid[x][y]==0:
                    for dx,dy in directions:
                        nx = x+dx
                        ny = y+dy
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                            connected_components.add(ds.find(nx*n+ny))
                    for i in connected_components:
                        total_size+=ds.size[i]
                max_islands = max(total_size+1,max_islands)

        return max_islands
