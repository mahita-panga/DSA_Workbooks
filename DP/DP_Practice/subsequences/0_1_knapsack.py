"""
0/1_Knapsack
You are given weights and values of N items, and put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.

Intuition:
    Recursion: Every val in the array has pick/not_pick. if picking, update the weight.

-> Express everything in terms of index,weight(W).
-> Explore all the possibilities
-> Return max of all possibilites.
"""

#RECURSION
class Solution:

    def knapsackUtil(self,index,W,wt,val):
        if index==0:
            if wt[index]<=W:
                return val[index]
            else:
                return 0
        notPick = 0 + self.knapsackUtil(index-1,W,wt,val)
        pick = float('-inf')
        if wt[index]<=W:
            pick = val[index]+self.knapsackUtil(index-1,W-wt[index],wt,val)
        return max(pick,notPick)

    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        N= len(wt)
        return self.knapsackUtil(N-1,W,wt,val)

#TC: O(2^n)
#SC: O(N)+O(N)


#MEMOIZATION
#NOTE: When declaring dp array size, ensure that we use space of W+1 instead of W.
# 2 variables are changing states here -> index,W <- 2D dp.
class Solution:

    def knapsackUtil(self,index,W,dp,wt,val):
        if index==0:
            if wt[index]<=W:
                return val[index]
            else:
                return 0
        if dp[index][W] != -1:
            return dp[index][W]

        notPick = 0 + self.knapsackUtil(index-1,W,dp,wt,val)
        pick = float('-inf')
        if wt[index]<=W:
            pick = val[index]+self.knapsackUtil(index-1,W-wt[index],dp,wt,val)

        dp[index][W] = max(pick,notPick)
        return dp[index][W]

    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        N= len(wt)
        dp = [[-1 for _ in range(W+1)] for _ in range(N)]
        return self.knapsackUtil(N-1,W,dp,wt,val)

#TC: O(N*W)
#SC: O(N*W)+O(N)-(ASS)

#TABULATION
# THIS SOLUTION IS GIVING TLE because of the for-loop 🥲
# In for loop, instead of iterating through weight space,
# we can just iterate from wt[0] to W, as we are just picking
# all weights >0th index and saving the value in it.
class Solution:
    def knapSack(self,W, wt, val):
        N= len(wt)
        dp = [[0 for _ in range(W+1)] for _ in range(N)]
        # CAUSE OF TLE 😭
        # for i in range(W+1):
        #     if wt[0]<=i:
        #         dp[0][i] = val[0]
        #     else:
        #         dp[0][i] = 0

        for i in range(wt[0],W+1):
            dp[0][i] = val[0]

        for i in range(1,N):
            for j in range(1,W+1):
                notPick = 0 + dp[i-1][j]
                pick = float('-inf')
                if wt[i]<=j:
                    pick = val[i]+dp[i-1][j-wt[i]]
                dp[i][j] = max(pick,notPick)
        return dp[N-1][W]


#TABULATION -SPACE OPTIMIZATION
class Solution:
    def knapSack(self,W, wt, val):
        N= len(wt)
        prev = [0 for _ in range(W+1)]
        for i in range(wt[0],W+1):
            prev[i] = val[0]
        #when you modify curr in the next iteration, it also modifies prev, leading to incorrect results.
        #You should create a new curr array at each iteration.
        for i in range(1,N):
            curr = [0 for _ in range(W+1)]
            for j in range(1,W+1):
                notPick = 0 + prev[j]
                pick = float('-inf')
                if wt[i]<=j:
                    pick = val[i]+prev[j-wt[i]]
                curr[j] = max(pick,notPick)
            prev = curr

        return prev[W]

#TABULATION IN-PLACE SPACE OPTIMIZATION:
# If we observe, we dont need to maintain the curr array, we just the value that can
# be updated in place for the prev array.
# Note, only iterating right to left would work because if we are doing left to right i.e.
# j from wt[i]-1 to W, we will be overriding the prev values/left which we need to consider
# but right to left is fine since the prev values will remain intact.

class SolutionBest:
    def knapSack(self,W, wt, val):
        N= len(wt)
        #dp = [[0 for _ in range(W+1)] for _ in range(N)]
        prev = [0 for _ in range(W+1)]
        for i in range(wt[0],W+1):
            prev[i] = val[0]

        for i in range(1,N):
            for j in range(W,wt[i]-1,-1):
                # notPick = 0 + prev[j] <- directly used in max()
                # pick = float('-inf')
                # if wt[i]<=j: <- THIS condition can be ensured in the iteration itself
                            # wt[i]-j<=0 means j should start from wt[i].
                            # Since we are using right to left, we start at W and go till wt[i]

                #   pick = val[i]+prev[j-wt[i]] <- used in max()
                prev[j] = max(val[i]+prev[j-wt[i]],prev[j])

        return prev[W]
