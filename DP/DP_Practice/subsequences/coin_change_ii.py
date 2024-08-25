"""
LC 518. Coin Change II

Find number of ways that you can get the amount. Similar to target sum except this is in positive space
so no need of doing the circus of bringing negative elements into positive space.

"""
#MEMOIZATION
class Solution:
    def coinChngUtil(self,index,amnt,coins,dp):
        if dp[index][amnt] != -1:
            return dp[index][amnt]

        if index==0:
            if amnt%coins[index]==0:
                return 1
            return 0

        notPick = self.coinChngUtil(index-1,amnt,coins,dp)
        pick = 0
        if coins[index]<=amnt:
            pick = self.coinChngUtil(index,amnt-coins[index],coins,dp)
        dp[index][amnt] = pick + notPick

        return dp[index][amnt]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1)  for _ in range(len(coins))]
        return self.coinChngUtil(len(coins)-1,amount,coins,dp)

# TABULATION
#
class TabSolution:
    def change(self, amount: int, coins: List[int]) -> int:
            dp = [[0] * (amount + 1)  for _ in range(len(coins))]

            #Base case:
            for i in range(amount+1):
                if i%coins[0] == 0:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0

            for i in range(1,len(coins)):
                for j in range(amount+1):
                    dp[i][j] = dp[i-1][j]
                    if coins[i] <= j:
                        dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

            return dp[len(coins)-1][amount]

    # We only need the element of previous row for same column. so instead of have 2 arrays
    # we can directly use dp where dp[k] which denotes the numbers of coins needed to achieve target k
    # instead of checking coins[i]<=j we can directly choose the sum/target to iterate from coins[i] to target
    # and check if we want to pick or not.

    def change_1D(self, amount: int, coins: List[int]) -> int:
            dp = [0] * (amount + 1)

            #Base case:

            dp[0] = 1 #one way to make amount 0 - choosing no coins

            for i in range(len(coins)):
                for j in range(coins[i],amount+1):
                    dp[j] = dp[j] + dp[j-coins[i]]

            return dp[amount]
