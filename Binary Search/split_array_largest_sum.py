"""
    Minimize the maximum sum of a partition
        - dp - dp[i][k] - min of largest sum when splitting first i elements in k partition
        something like this -
             dp[i][k] = min(dp[j][k-1], sum(nums[j:i])) for all j in [0, i)
        - O(n^2.k) - we compute subarray sums and iterate over all the partitions
        For given constraints - this is tooo big. TLE. So better one is

        -> Instead of figuring how to split the array, given a particular sum, can we split array into <=k paritions.
        If yes, we reduce the search space until it is not possible anymore
        annd if no we search in the right side.
        -- CLASSIC BINARY search

        -- Bounds : LB - max(arr) - max possible val in the array
                    UB - sum(arr) - what if we consider all ele in 1 partition i.e no split

        -- condition to check the possibility: "GREEDY" way of choosing the right parition.
            given a target sum, split the array into k partitions
            from lef to right
            for each num in array,
                if curr_sum>=max_sum:
                    create a new partition and rest curr_sum = curr_num
                    inc partition cnt

            if partition_cnt <= req partitions, return True else False
"""
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lb = max(nums)
        ub = sum(nums)

        def is_partition_possible(max_sum):
            curr_sum = 0
            par_cnt = 1 #DONT undercount the partition. One partition is definitely there
            for i in nums:
                if curr_sum + i > max_sum:
                    curr_sum = i
                    par_cnt+=1
                else:
                    curr_sum += i
            return par_cnt<=k

        ans = 0
        while lb<=ub: #We are trying to find the exact sum which helps us
            mid = (lb+ub)//2
            if is_partition_possible(mid):
                ans = mid
                ub = mid - 1
            else:
                lb = mid + 1

        return ans
