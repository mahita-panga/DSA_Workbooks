"""
70. Climbing Stairs

Rec solution:
    -> Given n, we have 2 options at every step i.e. go down 1 step or 2 steps.
     i.e. total possibilitied for every f(n) = f(n-1) + f(n-2)
     BASE CASE: when n=1/0, we count that as 1 step.

Memoization:
    -> To avoid calculations of same recursive value, we can leverage @cache annotaion which internally maintains a dp_array

    -> To understand the memoization, we consider dp_array all initialized to -1, stating the values are not calculated yet.
        if dp[n] != -1 i.e. it has already been calculated, we return dp[n]
        else:
            dp[n] = f(n-1,dp)+f(n-2,dp)

Tabulation:
    -> Instead of having the recursive calls made, we can create a tabular data which maintains the information at various
    indices calculated.
     -> Base values, dp[0] = 1, dp[1] =1
     -> Start calculation for all 2 to n+1:
         dp[i] = dp[i-1]+dp[i-2]
         At the end dp[n] stores the req. value

    -> In above, we are having a dp[] which takes O(N) space. To avoid, we can just consider 2 values prev1 and prev2.
    Using these, we can find the new values.
"""

# RECURSION SOLUTION -- (TLE)
class RecSolution:
    def f(self,n):
        if n==1 or n==0:
            return 1
        return self.f(n-1)+self.f(n-2)

    def climbStairs(self, n: int) -> int:
        return self.f(n)

# MEMOIZATION
class MemCacheSolution:
    @cache
    def f(self,n):
        if n==1 or n==0:
            return 1
        return self.f(n-1)+self.f(n-2)


    def climbStairs(self, n: int) -> int:
        return self.f(n)

#MEMOIZATION WITHOUT @CACHE
class MemSolution:
    def f(self,n,dp):
        if n<=1:
            return 1
        if dp[n] != -1:
            return dp[n]
        else:
            dp[n] =  self.f(n-1,dp)+self.f(n-2,dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1) #n+1 is considered for dp_array size because step starts 0.
        return self.f(n,dp)

#TABULATION
class TabSolution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

#TABULATION_SAVING_SPACE
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 1
        for i in range(2,n+1):
            curr = prev2+prev1
            prev2 = prev1   #NOTE: DONT MESS THE ORDER OF ASSIGNMENT
            prev1 = curr

        return prev1
