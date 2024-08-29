"""
     i
     |
rabbit
bit
  |
  j

 Possibilities:
    When s[i]==t[j]: we found a match. Either we can pick this matched character from s1
    and search for other chars or not pick and search for other chars
    Hence it would be: (pick) f(i-1,j-1) + (notpick) f(i-1,j)

    else: Since no match, we direct search for other characters
    in the string for the jth char: f(i-1,j)

Base case:
    if j<0: exhausted string2 i.e. match found. Hence return 1
    if i<0: exhausted str1 and str2 is still there, match not possible. Hence return 0.

"""
class Solution:
    def numDistinctUtil(self,i,j,s,t,dp):
        if j<0:
            return 1
        if i<0:
            return 0

        if dp[i][j]!= -1:
            return dp[i][j]

        if s[i]==t[j]:
            dp[i][j] = self.numDistinctUtil(i-1,j-1,s,t,dp) + self.numDistinctUtil(i-1,j,s,t,dp)
        else:
            dp[i][j] = self.numDistinctUtil(i-1,j,s,t,dp)

        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        dp = [[-1]*n for _ in range(m)]
        return self.numDistinctUtil(m-1,n-1,s,t,dp)

#TABULATION
class TabSolution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1


        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1]==t[j-1]:
                    dp[i][j]+= dp[i-1][j-1]
        return dp[m][n]
#TC O(MxN), SC O(MxN)
