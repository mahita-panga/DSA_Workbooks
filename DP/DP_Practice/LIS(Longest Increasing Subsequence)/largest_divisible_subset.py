"""
368. Largest Divisible Subset
Given a set of distinct positive integers nums, return the largest subset answer
such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

-> Similar to printing LCS
-> We are looking for Longest Divisible Subset(Subsequence in sorted array)
-> Since subset can be of any order, if we sort it -> becomes longest subsequence proble

->Condition to update db array: arr[i]%arr[j]==0
-> Add to dp array only if the dp[j]+1 > dp[i]
-> hash_arr is used to save the indexes of the array to backtrack.
"""
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        hash_arr = [-1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    hash_arr[i] = j

        idx = dp.index(max(dp))
        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = hash_arr[idx]
        return res[::-1]

print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
