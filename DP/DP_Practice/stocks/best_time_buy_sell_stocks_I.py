"""
BASIC PROBLEM
"""
#GREEDY APPROACH I DID LOONG BACK
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = min(prices)
        buy_index = prices.index(min(prices))
        if buy_index == len(prices)-1:
            return 0
        sell=max(prices[buy_index:])

        return sell-buy

# IT FAILS AT [2,4,1]
# Recursion/DP is way.  Here, it is simple maximization prob.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            minBuy = min(prices[i],minBuy)
            maxProfit = max(maxProfit,prices[i]-minBuy)
        return maxProfit
