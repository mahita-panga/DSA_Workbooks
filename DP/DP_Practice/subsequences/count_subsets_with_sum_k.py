"""
Given an array arr of size n of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 10^9+7.

Intuition:
    Recursive: Typical pick/notPick use case to identify whether to choose the element for the subset or not
    Similar to subest_sum_k problem except that we have to find total number of subsets that satisfy.
    So, in recursion while returning we are returning 1 when we reach the base case indicating we have found a path
    with the required sum.
    At the end will add up all the paths i.e for pick and notPick

    Memoization: Using a dp[][] since there are 2 variables index and target. We use this to memoize the recursive solution

    Tabulation.

"""
class Solution:
    def perfectSumUtil(self,index,s,arr,dp):
        if dp[index][s] != -1:
            return dp[index][s]

        if s==0:
            return 1
        if index==0:
            return 1 if arr[index]==s else 0

        notPick = self.perfectSumUtil(index-1,s,arr,dp)
        pick = 0
        if arr[index]<=s:
            pick = self.perfectSumUtil(index-1,s-arr[index],arr,dp)
        dp[index][s] = pick + notPick

        return dp[index][s]

	def perfectSum(self, arr, n, sum):
		# code here
		dp =[[-1 for _ in range(sum+1)] for _ in range(n)]
		return self.perfectSumUtil(n-1,sum,arr,dp)
