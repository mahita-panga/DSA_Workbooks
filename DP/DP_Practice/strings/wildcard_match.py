"""
44. Wildcard Matching

Base case: if i<0 and j<0: Both strings exhausted, return True
            if i<0 and we still have j i..e few chars left in p: make sure all p's are only * or else return False.
            if j<0 i.e. pattern is exhausted then return False.
Recursion:
    if either char matches or encounter ? : move indexes i and j by 1
    if p encounters a *: check by either moving i (assuming * is 0) or by moving j(assuming * takes up 1 char at every rec call)
    aced | ac*
       i     j
    -> ace|ac*          -       aced| ac
    -> ac|ac* or ace|ac         returns False as d!=c
    and so on. until we reach the base cases.
"""
#NOTE: In memoization, check for dp[i][j]!=-1 after writing the base cases
# because of range issues which can be avoided by checks in base case.

class Solution:
    def isMatchUtil(self,i,j,s,p,dp):

        if i<0 and j<0:
            return True
        if i<0:
            for tmp in range(j + 1):
                if p[tmp] != '*':
                    return False
            return True

        if j<0:
            return False

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == p[j] or p[j]=='?':
            dp[i][j] = self.isMatchUtil(i-1,j-1,s,p,dp)

        elif p[j] == '*':
            dp[i][j] = self.isMatchUtil(i-1,j,s,p,dp) or self.isMatchUtil(i,j-1,s,p,dp)
        else:
            dp[i][j] = False
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1]* len(p) for _ in range(len(s))]
        return self.isMatchUtil(len(s)-1,len(p)-1,s,p,dp)

s=""
p="****"
print(Solution().isMatch(s,p))

#Tabulation:
class TabSolution:
    def isMatch(self, s: str, p: str) -> bool:
            m ,n = len(s),len(p)
            dp = [[False]* (len(p)+1) for _ in range(len(s)+1)]

            dp[0][0] = True
            for j in range(1,n+1):
                flag = True
                for tmp in range(1,j + 1):
                    if p[tmp-1] != '*':
                        flag = False
                dp[0][j] = flag

            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s[i-1] == p[j-1] or p[j-1]=='?':
                        dp[i][j] = dp[i-1][j-1]

                    elif p[j-1] == '*':
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = False

            return dp[m][n]
