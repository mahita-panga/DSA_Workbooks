"""
https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/
Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.


"""

#Your task is to complete this function

class Solution:
    def maxLen(self, arr):
        #prefix sum logic
        #main idea - > if we find same prefix sum somewhere, then the subarray between these
        #prefixes is bound to be zero.
        max_len = 0
        pref_sum = {}
        sum_p = 0
        for ind,i in enumerate(arr):
            sum_p+=i
            #If the cumulative sum is 0, the subarray from the start to the current index has sum 0
            if sum_p==0:
                max_len = max(max_len,ind+1)
            if sum_p in pref_sum.keys():
                max_len = max(max_len,ind-pref_sum[sum_p])
            else:
                pref_sum[sum_p] = ind
            # print(pref_sum)
        return max_len
