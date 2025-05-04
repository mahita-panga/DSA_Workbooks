"""
Best Time to Buy and Sell Stock II
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Intuition:
    -> We can buy/sell stock at any point. We can sell only after buying.
    After buying, we cannot buy without selling.
    -> Maximizing profit means we need to recursively check all possibilities.
    -> Recursion:
        -> Express in terms of indices: i,buy/sell decision variable.
        ->If previously NOT bought, then:
            at any index, we have 2 decisions to calculate profit:
                -> Do not buy the stock - move to next index, buy is '0' as we have not bought
                    So, profit add is 0
                -> Buy the stock - move to next index, buy is 1
                    So, profit add is -ARR[i] as we have bought it
        -> ELSE (bought previously and now selling):
            at any index, we have 2 decisions to calculate profit:
            -> Do not sell the stock - move to next index, buy is '1' as we had bought
                So, profit add is 0
            -> Sell the stock - move to next index, buy is '0' - Ready to buy next stock
                So, profit add is +ARR[i] as we have sold it
        Maximize the profit in both case and see what needs to be done.

        Base case: When reached the end of array: return 0 as we have completed trading.

    TABULATION:
        For converting to tabulation, dp table is being filled from last day to day 0
        So, traverse from the reverse of the array.
        At day0 whatever max profit you get, that is the answer.
"""


#MEMOIZATION
class Solution:
    def maxProfitUtil(self, index, buy, prices, dp):

        if index == len(prices):
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0
        if buy == 0:  #BUY THE STOCK
            profit = max(self.maxProfitUtil(index + 1, 0, prices, dp),
                         self.maxProfitUtil(index + 1, 1, prices, dp) - prices[index])
        else:  #SELL THE STOCK
            profit = max(self.maxProfitUtil(index + 1, 1, prices, dp),
                         self.maxProfitUtil(index + 1, 0, prices, dp) + prices[index])

        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices))]
        return self.maxProfitUtil(0, 0, prices, dp)


#TABULATION
class TabSolution:

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices) + 1)]
        dp[len(prices)][0] = 0
        dp[len(prices)][1] = 0

        for i in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy == 0:
                    profit = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
                else:
                    profit = max(dp[i + 1][1], dp[i + 1][0] + prices[i])
                dp[i][buy] = profit
        return dp[0][0]
