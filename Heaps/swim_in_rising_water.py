"""
https://leetcode.com/problems/swim-in-rising-water

	•   Treat each move as a cost equal to the maximum elevation encountered so far.
	•	Use a min‑heap of nodes keyed by their elevation; always expand to the neighbor with the next smallest elevation.
	•	Keep track of max_elev_seen: your answer is the maximum elevation on your path when you reach the end.
	•	Efficiently finds the path that minimizes the “bottleneck” elevation you must wait for  ￼.
	•	Complexity: O(n² · log(n²)) ≈ O(n² log n).

"""

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0]*n for _ in range(n)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pq = [(grid[0][0],0,0)]
        time = grid[0][0]
        visited[0][0] = 1
        while pq:
            time,row,col = heapq.heappop(pq)
            if row==n-1 and col==n-1:
                return time
            for dx,dy in directions:
                nx = dx+row
                ny = dy+col
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]!=1:
                    visited[nx][ny] = 1
                    heapq.heappush(pq,(max(time,grid[nx][ny]),nx,ny))
        return -1
