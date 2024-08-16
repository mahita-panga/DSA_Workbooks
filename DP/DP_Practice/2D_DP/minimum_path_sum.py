"""
LC 64: https://leetcode.com/problems/minimum-path-sum/

Intuition:
    Greedy will not work because we might miss on the actual path with min sum
    Recursion : Top Down approach, find min of all sum
    Tabulation: Bottom Up Approach:
        First Rule: Initialize dp array of same size
        Second Rule: Define base case i.e. dp[0][0] = grid[0][0]
        Third Rule: Update dp table action:
            If i > 0, then up = dp[i-1][j], otherwise up is set to infinity (float('inf'))
            to ensure it won’t be considered in the min function.
            If j > 0, then left = dp[i][j-1], otherwise left is set to infinity for the same reason.

            The value of dp[i][j] is updated to the sum of the
            current grid value grid[i][j] and the minimum of up and left.

"""
#TABULATION
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[0][0]
                    continue
                up = float('inf')
                left = float('inf')
                if i>0:
                    up = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up,left)
        return dp[m-1][n-1]
