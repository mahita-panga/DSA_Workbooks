"""
1277. Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Intuition:
"""
from typing import List
class Solution:
    def countSquares(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        #dp[i][j] = no of squares that end at the right bottom
        for i in range(m):
            dp[i][0] = grid[i][0]
        for j in range(n):
            dp[0][j] = grid[0][j]

        directions = [(0,-1),(-1,-1),(-1,0)]
        for i in range(1,m):
            for j in range(1,n):
                min_sq = float('inf')
                if (grid[i][j] == 0):
                    dp[i][j] = 0
                else:
                    for dx,dy in directions:
                        nx = dx+i
                        ny = dy+j
                        if 0<=nx<m and 0<=ny<n:
                            min_sq = min(min_sq,dp[nx][ny])
                    dp[i][j] = 1+min_sq
        # print(dp)
        ans = 0
        for i in range(m):
            for j in range(n):
                ans+=dp[i][j]
        return ans
