"""
GFG: https://www.geeksforgeeks.org/problems/geek-jump/1
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair.
At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps
from a stair i to stair j, the energy consumed in the jump is " abs(height[i]- height[j]) ",
where abs() means the absolute difference.
We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.
"""
#MEMOIZATION
class Solution:
    def solve(self, ind, height, dp):
        if ind == 0:
            return 0
        if dp[ind] != -1:
            return dp[ind]

        print(f"Calculating dp[{ind}]")

        jumpOne = self.solve(ind-1, height, dp) + abs(height[ind] - height[ind-1])
        jumpTwo = float('inf')
        if ind > 1:
            jumpTwo = self.solve(ind-2, height, dp) + abs(height[ind] - height[ind-2])

        dp[ind] = min(jumpOne, jumpTwo)
        print(f"dp[{ind}] = {dp[ind]}")
        return dp[ind]

    def minimumEnergy(self, height, n):
        dp = [-1] * n  # Initialize dp with size n
        return self.solve(n-1, height, dp)

#########################################################################
# ABOVE IS CAUSING 'RECURSION DEPTH LIMITATION' ISSUE WITH LARGE INPUT. #
#########################################################################

#TABULATION
# Using dp_array to store energy. We know energy at 0 and 1.
# For all steps from 2 to n
# calculate total energy required to take this step
# Choose the minimum of them
class Solution:
    def minimumEnergy(self, height, n):
        if n == 0:
            return 0
        if n == 1:
            return 0

        dp = [0] * n #Stores the energy
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])

        for i in range(2, n):
            jumpOne = dp[i-1] + abs(height[i] - height[i-1])
            jumpTwo = dp[i-2] + abs(height[i] - height[i-2])
            dp[i] = min(jumpOne, jumpTwo)

        return dp[-1]

#TABULATION WITH SPACE OPTIMIZATION
class Solution:
    def minimumEnergy(self, height, n):
        if n == 0:
            return 0
        if n == 1:
            return 0


        prev2 = 0
        prev1 = abs(height[1] - height[0])

        for i in range(2, n):
            jumpOne = prev1 + abs(height[i] - height[i-1])
            jumpTwo = prev2 + abs(height[i] - height[i-2])
            curr = min(jumpOne, jumpTwo)
            prev2 = prev1
            prev1 = curr

        return prev1
