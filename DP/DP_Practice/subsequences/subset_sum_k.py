"""
GFG: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Intuition:
"""
#RECURSION
class Solution:
    def subsetSumUtil(self,i,arr,k):
        if arr[i] == k:
            return True
        if i == 0:
            return arr[i]==k #Ensure proper check is happening. When you reached 0th index,
            # we only have one element to compare. So return true/false if that ele is the target
        notPick = self.subsetSumUtil(i-1,arr,k)
        pick = False
        if arr[i]<=k:
            pick = self.subsetSumUtil(i-1,arr,k-arr[i])
        return pick or notPick

    def isSubsetSum (self, N, arr, sum):
        return self.subsetSumUtil(N-1,arr,sum)

#MEMOIZATION
# According to #1 in points_to_remember, we need a 2D dp array
# of dimensions Nx(k+1). N is total given elements and k+1 is tha spac
# to check if this number should be present in sum or not

class Solution:
    def subsetSumUtil(self,i,arr,k,dp):
        if k==0:
            return True
        # BELOW IF is redundant. if arr[i] == k, then k==0 in the next step.
        if arr[i] == k:
            return True
        if i == 0:
            return arr[i]==k

        if dp[i][k] != -1:
            return dp[i][k]

        notPick = self.subsetSumUtil(i-1,arr,k,dp)
        pick = False
        if arr[i]<=k:
            pick = self.subsetSumUtil(i-1,arr,k-arr[i],dp)
        dp[i][k] = pick or notPick

        return dp[i][k]

    def isSubsetSum (self, N, arr, sum):
        dp = [[-1 for _ in range(sum+1)] for _ in range(N)]
        return self.subsetSumUtil(N-1,arr,sum,dp)

"""
TC: O(NxK)
SC: O(NxK)+O(N)
"""
#TABULATION
# Dp array initialization
# Base case setup
# Copy recurrence relation of memoization and convert it to tabulation

class Solution:
    def isSubsetSum(self, N, arr, sum):
        # Initialize the DP table
        dp = [[False for _ in range(sum + 1)] for _ in range(N)]

        # Base case: A sum of 0 is always achievable by picking no elements
        for i in range(N):
            dp[i][0] = True

        # Base case for the first element
        if arr[0] <= sum:
            dp[0][arr[0]] = True

        # Fill the DP table
        for i in range(1, N):
            for j in range(1, sum + 1):
                notPick = dp[i - 1][j]  # If we don't pick the current element
                pick = False
                if arr[i] <= j:
                    pick = dp[i - 1][j - arr[i]]  # If we pick the current element

                dp[i][j] = pick or notPick  # Update the DP table

        return dp[N - 1][sum]

# arr = [3, 34, 4, 12, 5, 2]
# sum_val = 9
# print(Solution().isSubsetSum(len(arr), arr, sum_val))  # Output should be True


# SPACE OPTIMIZED TABULATION
# Thumb Rule:
    # Whenever you see ind-1, then it means we need a prev element
    # Here it is dp[ind-1] mean we need prev array and curr array
    # according to base case, prev[0] and curr[0] is True
    # replace dp[ind-1] with prev and dp[ind] with curr
    # prev = curr

class Solution:
    def isSubsetSum (self, N, arr, sum):
        prev = [False] * (sum + 1)


        prev[0] = True
        if arr[0]<=sum:
            prev[arr[0]] = True

        for i in range(1,N):
            curr = [False] * (sum + 1)
            curr[0] = True

            for j in range(1,sum+1):
                notPick = prev[j]
                pick = False
                if arr[i]<=j:
                    pick = prev[j-arr[i]]
                curr[j] = pick or notPick
            prev = curr

        return prev[sum]
