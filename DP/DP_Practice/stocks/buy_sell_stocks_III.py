"""
ATMOST 2 TRANSACTIONS<- condition
A transaction consists of buying and then later selling a stock.

Intuition:
    -> We need to keep a track of another variable called cap. Cap can not exceed 2.
    -> 2 variables:
        the current day (index),
        whether you’re holding a stock (buy), and
        the number of transactions left (cap).
    -> 3D DP : dp[index][buy][cap]
Memoization -> additional base case for cap.
Tabulation:
    -> We work backwards starting from n-1 to 0.
    -> cap and buy is from 1->3 and 0->2
    dp array at Cap 0 is 0. Hence doing it from 1->3.
    ->copy recurrence from memoization.
    -> return dp[0][0][2].


"""
from typing import List


class Solution:
    def maxProfitUtil(self,index,buy,cap,prices,dp):
        if cap==2:
            return 0
        if index == len(prices):
            return 0

        if dp[index][buy][cap] != -1:
            return dp[index][buy][cap]

        profit = 0
        if buy==0: #BUY THE STOCK
            profit = max(self.maxProfitUtil(index+1,0,cap,prices,dp),
                        self.maxProfitUtil(index+1,1,cap,prices,dp)-prices[index])
        else: #SELL THE STOCK
            profit = max(self.maxProfitUtil(index+1,1,cap,prices,dp),
                        self.maxProfitUtil(index+1,0,cap+1,prices,dp)+prices[index])

        dp[index][buy][cap] = profit
        return dp[index][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1]*2 for _ in range(2)] for _ in range(len(prices))]
        return self.maxProfitUtil(0,0,0,prices,dp)


#TABULATION
class TabSolution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0] * 3 for _ in range(2)] for _ in range(len(prices) + 1)]

        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 0:  # BUY THE STOCK
                        profit = max(dp[index + 1][0][cap],  # Skip buying
                                     dp[index + 1][1][cap] - prices[index])  # Buy
                    else:  # SELL THE STOCK
                        profit = max(dp[index + 1][1][cap],  # Skip selling
                                     dp[index + 1][0][cap - 1] + prices[index])  # Sell
                    dp[index][buy][cap] = profit

        return dp[0][0][2]

#TABULATION
class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0] * (k+1) for _ in range(2)] for _ in range(len(prices) + 1)]

        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
                    if buy == 0:  # BUY THE STOCK
                        profit = max(dp[index + 1][0][cap],  # Skip buying
                                     dp[index + 1][1][cap] - prices[index])  # Buy
                    else:  # SELL THE STOCK
                        profit = max(dp[index + 1][1][cap],  # Skip selling
                                     dp[index + 1][0][cap - 1] + prices[index])  # Sell
                    dp[index][buy][cap] = profit

        return dp[0][0][k]
