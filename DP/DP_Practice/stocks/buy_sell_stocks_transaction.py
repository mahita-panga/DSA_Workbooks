"""
WHEN SELLING THERE IS A TRANSACTION FEE
-> Condition here is that there is a transaction fee while selling the stock or completing the transaction
-> During sell, we will add the fee as sell indication the transaction is complete.

"""
#MEMOIZATION
class Solution:
    def maxProfitUtil(self,index,buy,prices,fee,dp):
        if index >= len(prices):
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0
        if buy == 0: #NEED TO BUY
            profit = max(self.maxProfitUtil(index+1,0,prices,fee,dp), # DONT BUY CURR STOCK
            self.maxProfitUtil(index+1,1,prices,fee,dp)-prices[index]) # BUY CURR STOCK
        else: #NEED TO SELL
            profit = max(self.maxProfitUtil(index+1,1,prices,fee,dp), # DONT SELL CURR STOCK
            self.maxProfitUtil(index+1,0,prices,fee,dp)+prices[index]-fee) # SELL CURR STOCK WITH FEE
        dp[index][buy] = profit

        return dp[index][buy]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]
        return self.maxProfitUtil(0,0,prices,fee,dp)

#TABULATION
class TabSolution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0]*2 for _ in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            dp[i][0] = max(dp[i+1][0], dp[i+1][1]-prices[i])
            dp[i][1] = max(dp[i+1][1], dp[i+1][0]+prices[i]-fee)
        return dp[0][0]
