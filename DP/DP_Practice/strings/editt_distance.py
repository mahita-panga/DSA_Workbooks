"""
72: EDIT DISTANCE https://leetcode.com/problems/edit-distance/description/

Intuition:
    Express in terms of indexes: i,j for s1 and s2
    Explore all possibilities:
        -> if s1[i] == s2[j]: when both have same char, just move to previous indices
            i
            |
        horse
        ros
          |
          j
        -> else: we have 3 options to check
            *** Insertion: insert s, i remains and j moves -1
            *** Deletion: delete e, i moves -1 and j remains
            *** Replace: replace e, i and j moves -1
            choose the best of 3 i.e. min of all 3 and add 1 indication one edit distance
    Base Case:
        if i<0 i.e. s1 is exhausted but we still have chars in s2, we simply insert all char of s2.
        so dist = j+1
        if j<0 i.e. s2 is exhausted but we still have chars in s1, we simply delete all char in s1
        so dist = i+1
    ---THIS Solves the problem---

"""
#MEMOIZATION
class Solution:
    def minDistUtil(self,i,j,s1,s2,dp):

        if i<0:
            return j+1
        if j<0:
            return i+1

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i]==s2[j]:
            dp[i][j] = self.minDistUtil(i-1,j-1,s1,s2,dp)
        else:
            #Insert
            insert = self.minDistUtil(i,j-1,s1,s2,dp)
            delete = self.minDistUtil(i-1,j,s1,s2,dp)
            replace = self.minDistUtil(i-1,j-1,s1,s2,dp)
            dp[i][j] = 1 + min(insert,delete,replace)
        return dp[i][j]


    def minDistance(self, s1: str, s2: str) -> int:
        m , n = len(s1), len(s2)
        dp = [[-1]*n for _ in range(m)]
        return self.minDistUtil(m-1,n-1,s1,s2,dp)

#TC: O(MxN) SC: O(MXN)+O(M+N)[A.S.S]

class TabSolution:
    def minDistance(self, s1: str, s2: str) -> int:
            m , n = len(s1), len(s2)
            dp = [[0]*(n+1) for _ in range(m+1)]
            for j in range(n+1):
                dp[0][j]=j

            for i in range(m+1):
                dp[i][0]=i

            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

            return dp[m][n]

    #TC: O(MxN), SC O(MxN)
    def so_minDistance(self, s1: str, s2: str) -> int:
        m , n = len(s1), len(s2)
        prev = [0]*(n+1)
        for j in range(n+1):
            prev[j]=j

        # for i in range(m+1):
        #     dp[i][0]=i

        for i in range(1,m+1):
            curr = [0]*(n+1)
            curr[0] = i
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(curr[j-1], prev[j], prev[j-1])
            prev = curr[:]

        return prev[n]
     #TC: O(MxN), SC O(N)
