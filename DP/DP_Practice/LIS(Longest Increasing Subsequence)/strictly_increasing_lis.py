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
