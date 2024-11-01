"""
Minimum Number of Removals to Make Mountain Array

LIS + LDS concept
-  Assume, you try to consider each item as the peak in the resultant array
- If you assume arr[i] as peak, then
   1. All elements on left will form a LIS
   2. All elements on right will form a LCS
   - Here LIS and LCS will omit the elements which dont follow the order (its LI-Subsequence and not LI-Subset)
   - Now, lis[i]+lcs[i] = length of the final array with arr[i] as peak, this length is what you want to maximise
   - More the final length of the array = lesser number of deletions
- Deletions needed to make arr having one peak at i = (N-lis[i]+lds[i]+1)

Compare deletions only when lis[i] and lds[0] both are > 1  because when either lis or lds = 0, means there are no elements to right or left of the cur peak assumed element
It should follow pattern: INCREASE -> PEAK -> DECREASE (INCREASE -> PEAK or PEAK -> DECREASE wont be considered as peak)
"""

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i],dp1[j]+1)
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i]>nums[j]:
                    dp2[i] = max(dp2[i],dp2[j]+1)
            # if dp1[i]==1 or dp2[i]==1: #CONDITION TO NOT ADD INCASE IT IS ONLY STRICTLY INC. OR DEC.
            #     continue

        min_removals = float('inf')
        for i in range(n):
            if dp1[i] > 1 and dp2[i]>1:
                min_removals = min(min_removals,n-dp1[i]-dp2[i]+1)

        return min_removals
