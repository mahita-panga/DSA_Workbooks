"""
GFG: https://www.geeksforgeeks.org/problems/number-of-islands/1
You are given a grid of size n x m and a list of operations where each operation
adds land at a specific cell. You need to count the number of islands after each operation.
An island is a group of connected 1s (land), and connections can happen vertically or horizontally.

-> After every action, we have to find number of islands : So Disjoint sets => Union Find
-> 4 directions of traversal

Intuition:
    -> We maintain a visited array to identify if any particular row/col has been
    added to our sets.
    -> For saving mxn matrix to a disjoint set, we need to convert the node into a integer
        => node_number for a give (i,j) = i * number of cols + j
    for a 3x4 matrix node numbers will be :
        0 1 2 3
        4 5 6 7  //at any given i,j says (1,1), node number is 1*4+1 = 5
        8 9 10 11
    -> We maintain a cnt variable which will tell us number of islands for query
    -> For any island node:
        - if it is not duplicate, Increase the count // Node is a island in itself
        - mark it visited
        - Check all 4 directions and only in valid nodes,
        if it can be connected. For checking connections use ds find()
            In case anywhere we find a node that we can connect to, we reduce the cnt
            since the island is being connected to another node.
        - append cnts to a list and return ans.

NOTE: When the ultimate parents are not same, then cnt =-1 as ww are merging the new island
to a existing island. Hence count reduces.
"""

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

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        ds = DSU(rows*cols)
        visited = [[0]*cols for _ in range(rows)]
        cnt = 0
        ans = []
        for u,v in operators:
            if visited[u][v] == 1:
                ans.append(cnt)
                continue
            visited[u][v] = 1
            cnt+=1
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for dx,dy in directions:
                nx = dx+u
                ny = dy+v

                if 0<=nx<rows and 0<=ny<cols:
                    if visited[nx][ny] == 1:
                        nodeNum = u*cols+v
                        newNodeNum = nx*cols+ny
                        if ds.find(nodeNum) != ds.find(newNodeNum):
                            #Both have different parent and they are in the same row/col. So should be connected
                            cnt-=1
                            ds.union(nodeNum,newNodeNum)
            ans.append(cnt)

        return ans
