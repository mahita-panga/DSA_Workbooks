"""
LC 120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.

INTUITION:
    Similar to minimum path sum, greedy will not work.
    Think of triangle as a matrix where all i>j is 0.
    Only catch is in base condition:
        The first cell of each row will only be reached by going left
        The last triangle cell i.e diagonal will only be reached by going
        diagonally above.
        Remaning all cells can be reached via left and diagonal traversal.

    NOTE: When returning, the minimum value to reach the last cell i.e. (n-1,n-1)
    is not stored in dp[n-1][n-1] but it is min(dp[n-1]) since the minimum position
    can end at any point in the last row.

"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0 for _ in range(m)] for _ in range(m)]

        dp[0][0] = triangle[0][0]
        for i in range(1 ,m):
            for j in range(i +1):
                if j==0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j==i:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i - 1][j - 1])
        return min(dp[m - 1])
