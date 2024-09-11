"""
LENGTH OF LIS
-> whenever there is subsequence, it means we need pick/no pick logic.
We need to ensure that we are picking an item after the chosen index.
For this we need to track the prev_index that has been choosen.
NOTE:
    Since prev_index can be -1 when we are starting,
    you can’t use it directly as an index.
    Instead, we’re supposed to use prev_index + 1 when accessing the dp table, Hence
    the space for prev_index becomes n+1.

"""
# Memoization
# As we are only printing the length, we will return 0+next item choice in case of not pick
# and 1 + next item choice in case of pick
# Ensure the ranges for prev_index are proper
class Solution:
    def lisUtil(self,index,prev_index,nums,dp):
        if index==len(nums):
            return 0

        if dp[index][prev_index+1] != -1:
            return dp[index][prev_index+1]

        notPick = 0 + self.lisUtil(index+1,prev_index,nums,dp) #Not Pick
        pick = notPick
        if prev_index==-1 or nums[index]>nums[prev_index]: #Pick
            pick = 1+self.lisUtil(index+1,index,nums,dp)
        dp[index][prev_index+1] = max(pick,notPick)
        return dp[index][prev_index+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1]*(len(nums)+1) for _ in range(len(nums))]
        return self.lisUtil(0,-1,nums,dp)

#TABULATION
class TabSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][prev_index + 1] will store the length of LIS starting from index i with prev_index
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Bottom-up tabulation from the last index to the first
        for index in range(n - 1, -1, -1):
            for prev_index in range(index - 1, -2, -1):  # prev_index goes from -1 to index-1
                # Option 1: Don't pick the current element
                notPick = dp[index + 1][prev_index + 1]

                # Option 2: Pick the current element if it's valid
                pick = 0
                if prev_index == -1 or nums[index] > nums[prev_index]:
                    pick = 1 + dp[index + 1][index + 1]

                # Store the result
                dp[index][prev_index + 1] = max(pick, notPick)

        # dp[0][0] holds the result, i.e., starting from index 0 with no previous element
        return dp[0][0]

# BEST SOLUTION - 1D TABULATION
# We need not do 2d dp array.
# Idea is to maintain a dp array which contains the len of the longest increasing
# subsequence so far for that element in the arr
# Initially set dp arr to 1 indicating the len of subseq as 1
# Traverse array, and for all its prev elements check if the curr num is > any of the
# elements in array -> If yes get the max of all prev elements > curr element  by 1 or the
# existing len.
# max of dp is the len of LIS
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
# TC: O(N^2) and SC: O(N)

# TC can further be brought down.
# BINARY SEARCH + DP
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/C++Python-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)/
