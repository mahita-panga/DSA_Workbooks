"""
LC 1020: Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Intuition:
    -> Seems similar like surrounded regions problem
    -> All boundary land cells(1's) and its connected cells should be eliminated to avoid falling
    -> Only land cells which are not connected to boundary 1's should be considered

    -> This is using BFS.
    -> Identify all boundary 1's and connected 1's. Mark them unsafe or with "2". Add to q
    -> Traverse all 4 directions and if any connection found, then that also is unsafe.

    -> Once done, count number of 1s in the grid. These are the safe 1's
"""
from collections import deque
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        def mark_boundary_ones(nx,ny):
            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                q.append((nx,ny))
                grid[nx][ny] = 2

        for i in range(m):
            mark_boundary_ones(i,0) #(1,0),(2,0) .. -> left boundary
            mark_boundary_ones(i,n-1) #(1,3),(2,3) .. -> right boundary

        for j in range(n):
            mark_boundary_ones(0,j) #(0,1),(0,2)(0,3).. -> top boundary
            mark_boundary_ones(m-1,j) #(3,0)(3,1)(3,3).. -> bottom boundary

        while len(q)!=0:
            i,j = q.popleft()
            for dx,dy in directions:
                nx, ny = i+dx, j+dy
                mark_boundary_ones(nx,ny)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res+=1

        return res
