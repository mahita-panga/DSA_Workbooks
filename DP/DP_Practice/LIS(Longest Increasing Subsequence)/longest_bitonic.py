"""

Longest Bitonic subsequence : https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1

A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. Return the maximum length of bitonic subsequence.
Ex: [1, 2, 5, 3, 2]

Intuition:
    Since, we are talking about the longest pattern sequence, it would be a variation of LIS.
    -> Bitonic means having strictly increasing and then strictly decreasing
        => LIS : strictly increasing : L -> R traversal
        => LDS: strictly decreasing : finding increasing from R -> L traversal
    -> We maintain two arrays dp1 and dp2
    -> dp1 : LIS , dp2 : LDS
    -> res = LIS + LDS - 1 (-1 for the common ele consideration)

    -> Ensure that addition happens only when it has both LIS and LDS. We dont want strictly IS or DS.

"""

from typing import List
class Solution:
    #LIS from left and right
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i],dp1[j]+1)
        res = 0
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i]>nums[j]:
                    dp2[i] = max(dp2[i],dp2[j]+1)
            if dp1[i]==1 or dp2[i]==1: #CONDITION TO NOT ADD INCASE IT IS ONLY STRICTLY INC. OR DEC.
                continue
            res = max(res,dp1[i]+dp2[i]-1)

        return res

# TC: O(N^2)
# SC: O(2*N)
# CAN OPTIMIZE FURTHER WITH BINARY SEARCH -> Patience Sorting (LIS using binary search),
# KEY IDEA: compute the LIS for both directions using binary search and maintain the result in dp1 and dp2

from typing import List
import bisect

class SO_Solution:
    def LongestBitonicSequence(self, n: int, nums: List[int]) -> int:

        # Function to compute LIS using binary search
        def calculate_lis(nums: List[int]) -> List[int]:
            lis = []
            dp = [0] * len(nums)

            for i in range(len(nums)):
                #Searches the element and fetches the left most index in case of duplicate.
                pos = bisect.bisect_left(lis, nums[i])
                if pos < len(lis):
                    lis[pos] = nums[i]
                else:
                    lis.append(nums[i])
                dp[i] = pos + 1
            return dp

        # LIS from the left
        dp1 = calculate_lis(nums)

        # LIS from the right (reverse the input array)
        dp2 = calculate_lis(nums[::-1])[::-1]

        # Calculate the Longest Bitonic Sequence
        res = 0
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:  # Ensure it's both increasing and decreasing
                res = max(res, dp1[i] + dp2[i] - 1)

        return res

# Example usage:
sol = Solution()
print(sol.LongestBitonicSequence(7, [1, 11, 2, 10, 4, 5, 2]))
