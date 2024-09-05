"""
"""
#MEMOIZATION
class Solution:
    def maxProfitUtil(self,index,buy,cap,prices,dp):
        if cap==0:
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
                        self.maxProfitUtil(index+1,0,cap-1,prices,dp)+prices[index])

        dp[index][buy][cap] = profit
        return dp[index][buy][cap]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(len(prices))]
        return self.maxProfitUtil(0,0,k,prices,dp)
