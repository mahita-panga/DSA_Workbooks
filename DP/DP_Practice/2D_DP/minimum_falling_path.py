"""
LC 931: Minimum Falling Path Sum

INTUITION:
    We have 3 directions to fall, down, diagonal left/diagonal right
    When we are at first column, we can fall down and diagonal right
    and vice versa at last column.

    Tabulation:
        Initialization:
            dp array is same size as matrix
        Action:
            - The dp[i][j] value is updated to the current matrix value matrix[i][j]
            plus the minimum value of the possible paths from the previous row.
            - For each element matrix[i][j], there are three possible cells in the previous row (i-1)
            that could contribute to the minimum path: directly above (j), top-left diagonal (j-1),
            and top-right diagonal (j+1).
            - Depending on whether j is at the edge of the matrix (leftmost or rightmost column), we take care to avoid out-of-bounds indexing.
        Result:
            The result is the minimum value in the last row of the dp array,
            representing the minimum falling path sum from the top to the bottom of the matrix.
"""
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1,n):
            for j in range(n):
                if j==0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                elif j==n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
        return min(dp[n-1])
