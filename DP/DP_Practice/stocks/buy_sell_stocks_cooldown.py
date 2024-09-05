"""
BUY AND SELL WITH COOLDOWN
-> Condition: After selling, there should be a cooldown of 1 day

Intuition:
    -> Since this is only a condition while selling, we will ensure that
    During sell :
        i.e. buy==1 which mean we have bought a stock prev. and
    we need to sell,
    We will do f(index+2,0) -> indicating that we will decide to buy a stock after skipping a day.

    -> Since we are doing index+2, in base case handle it via index>=len then return 0.

"""
#MEMOIZATION
class Solution:
    def maxProfitUtil(self,index,buy,prices,dp):
        if index >= len(prices):
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0
        if buy == 0: #NEED TO BUY
            profit = max(self.maxProfitUtil(index+1,0,prices,dp), # DONT BUY CURR STOCK
            self.maxProfitUtil(index+1,1,prices,dp)-prices[index]) # BUY CURR STOCK
        else: #NEED TO SELL
            profit = max(self.maxProfitUtil(index+1,1,prices,dp), # DONT SELL CURR STOCK
            self.maxProfitUtil(index+2,0,prices,dp)+prices[index]) # SELL CURR STOCK WITH COOLDOWN
        dp[index][buy] = profit

        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]
        return self.maxProfitUtil(0,0,prices,dp)

#Tabulation
class TabSolution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices)+2)] #DP TABLE FOR len+2 space to accomodate the cooldown
        #BASE CASE: On last day, buy and sell decisions would be 0 as a transaction could not be
        #completed
        for index in range(len(prices)-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy==0:
                    profit = max(dp[index+1][0], #DONT BUY
                    dp[index+1][1] - prices[index]) #BUY
                else:
                    profit = max(dp[index+1][1], #DONT SELL
                    dp[index+2][0] + prices[index]) #SELL WITH COOLDOWN
                dp[index][buy] = profit

        return dp[0][0]

    def so_maxProfit(self, prices: List[int]) -> int:
        # Since our approach is forward looking i.e. curr buy/sell state depends on
        # the values ahead, we need front2 and front1.
        # front2 is for handling the cooldown
        # | d | a | b | c |
        #      curr f1  f2   <- Day n
        #  curr f1  f2       <- Day n-1
        # Hence f2 = f1.copy() and f1 = curr.copy()
        front2 = [0]*2
        front1 = [0]*2
        curr = [0]*2

        for index in range(len(prices)-1,-1,-1):
            curr[0] = max(front1[0], #DONT BUY
            front1[1] - prices[index]) #BUY

            curr[1] = max(front1[1], #DONT SELL
            front2[0] + prices[index]) #SELL WITH COOLDOWN

            front2 = front1.copy()
            front1 = curr.copy()
        return curr[0]
