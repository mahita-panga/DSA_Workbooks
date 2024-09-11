"""
LC 2035. Partition Array Into Two Arrays to Minimize Sum Difference

*** THIS IS NOT A DP PROBLEM ***

Why DP FAILS:
DP fails becuase we

What to do:
    Meet In the Middle : Tweaked formed of binary search
    MIM approach needs to use :
        -> Partitioning the arr into 2 eq halves.
        -> Bit Masking to find subsets in each part
        -> Binary search to find the relevant sum of the subset in second half.


"""

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        S = sum(nums)
        N = len(nums)
        offset = abs(min(0,S//2))

        dp = [[False for _ in range( S//2 + offset + 1)] for _ in range(N)]

        for i in range(N):
            dp[i][0] = True

        if nums[0]<= S//2:
            dp[0][nums[0]] = True
        min_sum = float('inf')
        for i in range(1,N):
            for j in range(S//2 + 1):
                notPick = dp[i-1][j]
                pick = False
                if nums[i]<=j:
                    pick = dp[i-1][j-nums[i]]
                dp[i][j] = pick or notPick


        for j in range(S//2 + 1):
            if dp[N-1][j] == True:
                    S1 = j
                    S2 = S-S1
                    min_sum = min(min_sum,abs(S1-S2))

        return min_sum
