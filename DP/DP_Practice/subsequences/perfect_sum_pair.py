"""


"""
class Solution:

    def perfectSumUtil(self, index, s, arr, dp):
        if dp[index][s] != -1:
            return dp[index][s]

        if arr[index] == s:
            return 1

        if index == 0: 
            return 1 if arr[0] == s or s == 0 else 0

        notPick = self.perfectSumUtil(index - 1, s, arr, dp)
        pick = 0
        if arr[index] <= s:
            pick = self.perfectSumUtil(index - 1, s - arr[index], arr, dp)
        dp[index][s] = pick + notPick

        return dp[index][s]

    def perfectSum(self, arr, n, sum):
        # code here
        dp = [[-1 for _ in range(sum + 1)] for _ in range(n)]
        return self.perfectSumUtil(n - 1, sum, arr, dp)

class TabSolution:
    def perfectSum(self, arr, n, sum):
        # code here
        dp = [[0 for _ in range(sum + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        if arr[0] <= sum:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            for j in range(sum + 1):
                np = dp[i - 1][j]
                p = 0
                if arr[i] <= j:
                    p = dp[i - 1][j - arr[i]]
                dp[i][j] = np + p

        return dp[n - 1][sum]
# n=10
# sum =31
# arr= [9,7,0,3,9,8,6,5,7,6]
n = 9
arr = [1, 0, 0, 0, 0, 0,0,0,0]
sum = 1
print(TabSolution().perfectSum(arr,n,sum))

# ABOVE SOLUTIONS WERE NOT WORKING, BELOW IS WORKING
# N+1 space consideration is working ??? WHY
class Solution:
    def perfectSum(self, arr, n, sum):
        mod = 1000000007

        # Create a 2D dp array where dp[i][j] represents the number of ways
        # to get sum j using the first i elements
        dp = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]

        # There's one way to get sum 0: using an empty subset
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]) % mod
                else:
                    dp[i][j] = dp[i - 1][j] % mod

        return dp[n][sum] % mod