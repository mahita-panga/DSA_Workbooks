"""
Count the number of LIS
-> Keep a count array to keep track of the counts.
cnt[i]: Stores the count that can be achieved at i
dp[i] : Stores the length of LIS that can be achieved at i.

If we are updating the dp table, then cnt remains same but if
we are satisfying the LIS condition but the dp table is not increasing,
then cnt increasing -> meaning that we have cnt+1 ways of arriving at this.

At end, just get the total of counts where dp[i] == max(dp) indicating LIS.
->

"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        cnt = [1] * len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    cnt[i] = cnt[j]

                elif nums[j]<nums[i] and dp[j]+1 == dp[i]:
                    cnt[i] += cnt[j]

        maxi = max(dp)
        cnti = 0
        for i in range(len(nums)):
            if dp[i]==maxi:
                cnti += cnt[i]

        return cnti
