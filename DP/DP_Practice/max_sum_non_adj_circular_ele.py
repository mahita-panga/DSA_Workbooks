"""
Problem Statement: Dynamic Programming: House Robber (DP 6)
LC: https://leetcode.com/problems/house-robber-ii/description/
Circular queue
Intuition:
    -> Only catch is the last and first element could be together.
    Key here is to split the problem into 2 sub problems i.e.
    * 1: Consider robbing houses from the first house to the second-last house
    (i.e., nums[0] to nums[n-2]).
	* 2: Consider robbing houses from the second house to the last house
	(i.e., nums[1] to nums[n-1]).


"""

#MEMOIZATION:
from typing import List
class Solution:
    @cache
    def max_amount(self,index,arr):
        if index == 0:
            return arr[index]
        if index<1:
            return 0
        pick = arr[index] + self.max_amount(index-2,arr)
        not_pick = 0 + self.max_amount(index-1,arr)
        return max(pick,not_pick)

    def rob(self,circular_array: List) -> int:
        n = len(circular_array)
        if n==0:
            return 0
        if n==1:
            return circular_array[0]
        subproblem1 = self.max_amount(n-2, circular_array[:n-1])
        subproblem2 = self.max_amount(n-2, circular_array[1:n])
        return max(subproblem1,subproblem2)

#MEMOIZATION with dp_array:
#NOTE: USE two dp arrays to avoid interferences instead of 1

from typing import List
class Solution:
    def max_amount(self,index,arr,dp,n):
        if dp[index] != -1:
            return dp[index]
        if index == 0:
            return arr[index]
        if index<0:
            return 0
        pick = arr[index] + self.max_amount(index-2,arr,dp,n)
        not_pick = 0 + self.max_amount(index-1,arr,dp,n)
        dp[index] = max(pick,not_pick)
        return dp[index]

    def rob(self,circular_array: List) -> int:
        n = len(circular_array)
        if n==0:
            return 0
        if n==1:
            return circular_array[0]
        dp1 = [-1]*(n-1)
        dp2 = [-1]*(n-1)
        subproblem1 = self.max_amount(n-2, circular_array[:n-1],dp1,n)
        subproblem2 = self.max_amount(n-2, circular_array[1:n],dp2,n)
        return max(subproblem1,subproblem2)

# TABULATION
#
class Solution:
    def max_sum(self,nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0],nums[1])

        for i in range(2,n):
            pick = nums[i] + prev2
            no_pick = 0 + prev1
            curr_i = max(pick,no_pick)
            prev2 = prev1
            prev1 = curr_i
        return prev1

    def rob(self,circular_array: List) -> int:
        n = len(circular_array)
        if n==0:
            return 0
        if n==1:
            return circular_array[0]
        sub_prob1 = self.max_sum(circular_array[:n-1])
        sub_prob2 = self.max_sum(circular_array[1:n])
        return max(sub_prob1,sub_prob2)
