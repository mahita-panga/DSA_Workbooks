"""
PRINTING THE LIS
We maintain a index array which will tell us where to navigate when printing the array.
-> This index array will initially have '-1' Whenever we are increasing the count in dp table,
we also update the the index responsible for the increment in the index array.
-> Post that, just get the index where max(dp) is present and from that index keep backtracking.
-> Since we backtracked, reverse the list
"""
class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        # Code here
        dp = [1]*N
        index = [-1]*N
        max_i = 0
        for i in range(1,N):
            for j in range(i):
                if arr[i]>arr[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        index[i] = j

        max_i = dp.index(max(dp))
        res = []
        while max_i!=-1:
            res.append(arr[max_i])
            max_i = index[max_i]

        return res[::-1]
