"""
https://www.geeksforgeeks.org/problems/chocolates-pickup/1
You have two robots that can collect chocolates for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of chocolates collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all chocolates, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the chocolates.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid

"""
#User function Template for python3

class Solution:
    def maxChocoUtil(self,i, j1, j2, n, m, grid, dp):
        # Base cases:
        # - If either of the indices is out of bounds, return a large negative value
        # - If we're at the last row, return the sum of chocolates in the two selected columns
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return float('-inf')

        if i == n - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        # If the result for these indices has already been computed, return it
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        # Initialize the maximum chocolates collected to a large negative value
        maxi = -sys.maxsize

        # Iterate through the adjacent cells in the next row
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ans = 0
                if j1 == j2:
                    ans = grid[i][j1] + self.maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
                else:
                    ans = grid[i][j1] + grid[i][j2] + self.maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
                maxi = max(maxi, ans)

        # Store the maximum chocolates collected in the memoization table
        dp[i][j1][j2] = maxi
        return maxi

    def solve(self, n, m, grid):
        dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]

        # Start the recursion from the first row, columns 0 and m-1
        return self.maxChocoUtil(0, 0, m - 1, n, m, grid, dp)
            # Code here
