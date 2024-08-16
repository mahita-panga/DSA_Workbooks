"""
LC 63: https://leetcode.com/problems/unique-paths-ii/description/

INTUITION SAME AS TOTAL UNIQUE PATH PROBLEM:
    except when we find a obstacle, we set dp[i][j] = 0
    i.e we will not explore that path further

"""
#TABULATION
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                up = 0
                left = 0
                if i>0:
                    up = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
                dp[i][j] = up + left
        return dp[m-1][n-1]
