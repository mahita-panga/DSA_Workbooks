"""
We can pick an item any number of times.

Intuition:
    -> Since we can pick the item any number of times, we will pick the same in 'Pick' condition
    i.e. pick = max(pick, index+W-weight(index))
    To avoid going into infinite loop, we will be handling the base case
    -> Base case:
        if index == 0:
                //We can pick the item at an index if its weight is less than current bag's Weight
                //and we can pick it only as many times as W/w[0] ...if we have W as 11, and w[0] as 3
                //then we can choose w[0] 3 times..
            return (W//wt[index])*val[index]

"""

#Memoization
class Solution:
    def knapsackUtil(self,index,W,val,wt,dp):
        if dp[index][W] != -1:
            return dp[index][W]

        if index==0:
            if wt[index]<=W:
                return (W//wt[index])*val[index]
            else:
                return 0

        notpick = 0 + self.knapsackUtil(index-1,W,val,wt,dp)
        pick = float('-inf')
        if wt[index]<=W:
            pick = val[index] + self.knapsackUtil(index,W-wt[index],val,wt,dp)
        dp[index][W] = max(pick,notpick)
        return dp[index][W]

    def knapSack(self, N, W, val, wt):
        # code here
        dp = [[-1 for _ in range(W+1)] for _ in range(N)]
        return self.knapsackUtil(N-1,W,val,wt,dp)

#TC: O(N*W)
#SC: O(N*W) + O(N)


#TABULATION
class Solution:
    def knapSack(self, N, W, val, wt):
            # code here
            dp = [[0 for _ in range(W+1)] for _ in range(N)]
            #return self.knapsackUtil(N-1,W,val,wt,dp)

            for i in range(wt[0],W+1):
                dp[0][i] = (i//wt[0])*val[0] #	dp[0][i] = (W//wt[0]) * val[0] should actually be dp[0][i] = (i//wt[0]) * val[0], because you need to calculate the value for the specific capacity i, not for the entire knapsack capacity W.


            for i in range(1,N):
                for j in range(1,W+1):
                    pick = float('-inf')
                    if wt[i]<= j :
                        pick = val[i]+dp[i][j-wt[i]]
                    dp[i][j] = max(dp[i-1][j], pick )

            return dp[N-1][W]

#SPACE OPTIMIZATION only 1 1-D array.
#we clearly see the values required:  dp[i-1][j] and dp[i-1][j - wt[i]],
# we can say that if we are at a column j, we will only require the values
# from the previous row of the same column and other values will be
#  from the cur row itself. So we need not store an entire array for i
#
# After calculating the cur[i] value we store it at the cur[i] position
#  so this cur[i] will automatically serve as preValue for the next row.
#  In this way, we space-optimize the tabulation approach by just using one row.
def knapSack(self, N, W, val, wt):
      # code here
      # dp = [[0 for _ in range(W+1)] for _ in range(N)]
      curr = [0]*(W+1)

      #return self.knapsackUtil(N-1,W,val,wt,dp)

      for i in range(wt[0],W+1):
          curr[i] = (i//wt[0])*val[0] #	dp[0][i] = (W//wt[0]) * val[0] should actually be dp[0][i] = (i//wt[0]) * val[0], because you need to calculate the value for the specific capacity i, not for the entire knapsack capacity W.


      for i in range(1,N):
          for j in range(1,W+1):
              pick = float('-inf')
              if wt[i]<=j:
                  pick = val[i]+curr[j-wt[i]]
              curr[j] = max(curr[j], pick)

      return curr[W]
