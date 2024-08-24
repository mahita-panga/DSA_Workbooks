"""
LC 416:

Intuition:
    Paritioning to two subsets with equal sum means finding one subset of len n/2 with sum S/2.
    This is similar to subset sum of k, except that we are search for subarray with sum S/2
"""
from typing import List
#Memoization
class Solution:
    def partitionUtil(self,index,s,nums,dp):
        if dp[index][s] != -1:
            return dp[index][s]

        if index==0:
            return nums[0] == s


        notPick = self.partitionUtil(index-1,s,nums,dp)
        pick = False
        if nums[index] <= s:
            pick = self.partitionUtil(index-1,s-nums[index],nums,dp)
        dp[index][s] = pick or notPick

        return dp[index][s]

    def canPartition(self, nums: List[int]) -> bool:

        N = len(nums)
        S = sum(nums)
        if S%2 != 0:
            return False

        dp = [[-1 for _ in range((S//2)+1)] for _ in range(N)]
        return self.partitionUtil(N-1,S//2,nums,dp)


#TABULATION
def canPartitionTab(self, nums: List[int]) -> bool:

        N = len(nums)
        S = sum(nums)
        if S%2 != 0:
            return False

        dp = [[False for _ in range((S//2)+1)] for _ in range(N)]
        dp[0][0] = True
        if nums[0]<= S//2:
            dp[0][nums[0]] = True

        for i in range(1,N):
            for j in range(S//2+1):
                notPick = dp[i-1][j]
                pick = False
                if nums[i] <= j:
                    pick = dp[i-1][j-nums[i]]
                dp[i][j] = pick or notPick
        return dp[N-1][S//2]

#TC: O(N*S)
#SC: O(NxS) + O(N)

#Space Optimized - General
def canPartitionSO(self, nums: List[int]) -> bool:

        N = len(nums)
        S = sum(nums)
        if S%2 != 0:
            return False

        # dp = [[False for _ in range((S//2)+1)] for _ in range(N)]
        prev = [False for _ in range((S//2)+1)]

        prev[0] = True
        if nums[0]<= S//2:
           prev[nums[0]] = True

        for i in range(1,N):
            curr = [False for _ in range((S//2)+1)]
            for j in range(S//2+1):
                notPick = prev[j]
                pick = False
                if nums[i] <= j:
                    pick = prev[j-nums[i]]
                curr[j] = pick or notPick
            prev = curr

        return prev[S//2]

#Space Optimized - Further
# Can be done to have one array and in-place replacement.
# KEY: Need to traverse the array in reverse.

def canPartitionSOBest(self, nums: List[int]) -> bool:
    N = len(nums)
    S = sum(nums)
    if S%2 != 0:
        return False

    # dp = [[False for _ in range((S//2)+1)] for _ in range(N)]
    curr = [False for _ in range((S//2)+1)]

    curr[0] = True
    if nums[0]<= S//2:
        curr[nums[0]] = True

        for i in range(1,N):
            #curr = [False for _ in range((S//2)+1)]
            for j in range(S//2,nums[i]-1,-1):
                curr[j] = curr[j-nums[i]] or curr[j]

        return curr[S//2]
