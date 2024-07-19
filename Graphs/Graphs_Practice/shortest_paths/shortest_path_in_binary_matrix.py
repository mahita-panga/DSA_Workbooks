"""
LC #1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

INTUITION:
    -> Since it is a unit weight, we can use a normal queue with dijkstra's rather than the priority queue approach.
    -> Keep track of the distance and when you reach the end, return the distance. In case you are unable to reach the end , return -1
    -> NOTE: Remember to add edge cases.

"""
from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        m = len(grid)
        n = len(grid[0])

        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque()
        new_dist = 1
        q.append((new_dist,(0,0)))
        dist[0][0] = 1

        while q:
            curr_dist, curr_node = q.popleft()
            if curr_node[0] == n-1 and curr_node[1]==n-1:
                return curr_dist
            for dx,dy in directions:
                nx = dx + curr_node[0]
                ny = dy + curr_node[1]
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 0:
                    new_dist = curr_dist + 1
                    if new_dist < dist[nx][ny]:
                        dist[nx][ny] = new_dist
                        q.append((new_dist,[nx,ny]))


        return -1
