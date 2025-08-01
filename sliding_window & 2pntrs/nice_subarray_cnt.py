"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Convert this into binary sub array of sum k problem
        # all evens ->0 odds -> 1
        # now [1,1,2,1,1] -> [1,1,0,1,1] -> find number of subarrays with cnt/sum = k
        #this time, using prefix 0's cnt to find the total count - Trick 3 in binary sub array sumk problem editorial

        """
        - sliding window to see if curr_sum==k or >k
        - if ==k, check if any leading zeroes at l ptr, is yes cnt how many and move l ptr
        - if >k, move l ptr and reduce curr_sum accordingly
        - after all this, total_cnt is updated with 1+prefix_zeros i.e. 2 zeros found, 3 possiblilities for that subarray

        """

        bin_nums = [0 if x%2==0 else 1 for x in nums]
        curr_cnt = 0
        tot_cnt = 0
        prefix_zeros = 0
        l = 0

        for r in range(len(nums)):
            curr_cnt += bin_nums[r]

            if bin_nums[r]==1:
                pref_zeroes = 0

            while curr_cnt>k:
                curr_cnt-=bin_nums[l]
                l+=1
                prefix_zeros = 0

            while curr_cnt==k and bin_nums[l]==0:
                prefix_zeros+=1
                l+=1

            if curr_cnt==k:
                tot_cnt+= (1+prefix_zeros)

        return tot_cnt
