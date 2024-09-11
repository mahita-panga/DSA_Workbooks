"""
LC 62: https://leetcode.com/problems/unique-paths/
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Intuition:
    RECURSION: As we follow top down approach, we will start at last node and move either
    left or up and when we reach the source ie. (0,0), we will return 1
    We will sum all paths that we reached source from destination
    Handle base cases i.e. whenever i<0 or j<0, then return 0

    MEMOIZATION:
    To avoid calculating subproblem, we will use dp array which is same size as the input

    TABULATION:
        # Declare same size array input
        # Initialize array with base cases i.e.
        #
        Ensure proper initialization is done.


"""
#RECURSION
class Solution:
    def countTotalWays(self,i,j,m,n):
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0

        return self.countTotalWays(i-1,j,m,n)+ self.countTotalWays(i,j-1,m,n)

    def uniquePaths(self, m: int, n: int) -> int:
        return self.countTotalWays(m-1,n-1,m,n)

#MEMOIZATION
class Solution:
    def countTotalWays(self,i,j,dp,m,n):
        if dp[i][j] != -1:
            return dp[i][j]
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0

        dp[i][j] = self.countTotalWays(i-1,j,dp,m,n)+ self.countTotalWays(i,j-1,dp,m,n)
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.countTotalWays(m-1,n-1,dp,m,n)


#TABULATION
class Solution:
    def uniquePaths(self,m,n):
        """
        Initialization of the DP Table:
       	•	The DP table dp[i][j] stores the number of unique paths to reach the cell (i, j) from the top-left corner (0, 0).
       	•	dp[i][0] is initialized to 1 for all i,
        as there’s only one way to reach any cell in the first column: moving down from the cell above.
       	•	dp[0][j] is initialized to 1 for all j,
        as there’s only one way to reach any cell in the first row: moving right from the cell to the left.
        """
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        ## MISTAKE: INITIALIZING ONLY SOURCE AS 1 is wrong
        ## dp[0][0] = 1
        ## REASON: Since there is only one way to reach any cell in the
        ##  first row or the first column

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
