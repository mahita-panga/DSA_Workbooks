"""
322. Coin Change

INTUITION: Similar to unbounded knapsack idea.

Base case: when the index is 0 and we have to pick a target of k, we will choose this only the arr[0] denomination can be used.
hence the condition to check the divisibility.

"""

#MEMOIZATION
class Solution:
    def coinChngUtil(self,index,amnt,coins,dp):
        if dp[index][amnt] != -1:
            return dp[index][amnt]

        if index==0:
            if amnt%coins[index]==0:
                return amnt//coins[index]
            return 10**5

        notPick = self.coinChngUtil(index-1,amnt,coins,dp)
        pick = notPick
        if coins[index]<=amnt:
            pick = 1 + self.coinChngUtil(index,amnt-coins[index],coins,dp)
        dp[index][amnt] = min(pick,notPick)

        return dp[index][amnt]


    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * (amount + 1)  for _ in range(len(coins))]
        ans = self.coinChngUtil(len(coins)-1,amount,coins,dp)
        if ans == 10**5:
            return -1
        return ans

#Tabulation
class TabSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            dp = [[0] * (amount + 1)  for _ in range(len(coins))]
            #ans = self.coinChngUtil(len(coins)-1,amount,coins,dp)

            for i in range(amount+1):
                if i%coins[0] == 0:
                    dp[0][i] = i//coins[0]
                else:
                    dp[0][i] = 10**5


            for i in range(1,len(coins)):
                for j in range(amount+1):
                    np = dp[i-1][j]
                    p = np
                    if coins[i] <= j:
                        p = 1 + dp[i][j-coins[i]]
                    dp[i][j] = min(np,p)

            if dp[len(coins)-1][amount]==10**5:
                return -1
            return dp[len(coins)-1][amount]

    #Space-Optimized
    def arr_coinChange(self, coins: List[int], amount: int) -> int:
            prev = [0] * (amount + 1)
            #ans = self.coinChngUtil(len(coins)-1,amount,coins,dp)

            for i in range(amount+1):
                if i%coins[0] == 0:
                   prev[i] = i//coins[0]
                else:
                    prev[i] = 10**5


            for i in range(1,len(coins)):
                curr = [0] * (amount + 1)
                for j in range(amount+1):
                    np = prev[j]
                    p = np
                    if coins[i] <= j:
                        p = 1 + curr[j-coins[i]]
                    curr[j] = min(np,p)
                prev = curr

            if prev[amount]==10**5:
                return -1
            return prev[amount]

    def coinChange_1D(self, coins: List[int], amount: int) -> int:
        dp = [10**5] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            # NOTE: If you start iterating from j = 0, for amounts less than coins# [i], it’s not possible to include coins[i] in the sum because coins[i] itself is greater than the current amount j.
            # Therefore, for any j < coins[i], the value of dp[j] cannot be updated by using coins[i] (it would stay as it was from previous iterations).
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j],1 + dp[j-coins[i]])

        if dp[amount] == 10**5:
            return -1
        return dp[amount]
