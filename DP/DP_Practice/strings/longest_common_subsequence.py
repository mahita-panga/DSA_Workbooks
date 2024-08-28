"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

Intuition:
    RECURSION:
        1. Express in terms of indices:
            We have two indexes i1 and i2 looking at two strings.
            we will try to see if it is a match or no match.
        2. Explore possibilities: Match / Not Match
        If matched: add 1 to the result and reduce both indexes by 1
        If not match: reduces i1 by 1 and i2 remains same, check and vice versa.
        (ac |ca
        i1  i2  --> If we move i1 and i2 remains, then we find a match and viceversa.
        We need to take the max of both these paths.)
        3. Base case: when index<0: then dont explore that path.

        TC: O(2^n * 2^m)



"""

#RECURSION
class Solution:
    def lcsUtil(self,i1,i2,s1,s2):
        if i1<0 or i2<0:
            return 0
        if s1[i1] == s2[i2]:
            return 1+self.lcsUtil(i1-1,i2-1,s1,s2)
        else:
            return max(self.lcsUtil(i1,i2-1,s1,s2), self.lcsUtil(i1-1,i2,s1,s2))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcsUtil(len(text1)-1,len(text2)-1,text1,text2)

#MEMOIZATION:
class MemSolution:
    def lcsUtil(self,i,j,s1,s2,dp):
        if dp[i][j] != -1:
            return dp[i][j]

        if i<0 or j<0:
            return 0
        if s1[i] == s2[j]:
            dp[i][j] = 1+self.lcsUtil(i-1,j-1,s1,s2,dp)
        else:
            dp[i][j]=max(self.lcsUtil(i,j-1,s1,s2,dp), self.lcsUtil(i-1,j,s1,s2,dp))

        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*len(text2) for _ in range(len(text1))]
        return self.lcsUtil(len(text1)-1,len(text2)-1,text1,text2,dp)

#TABULATION:
# DP TABLE dp[i][j] denotes the match obtained at str1 of length i and str2 of length j
# We need to consider m+1 and n+1 space to include the match at length 0.
# This will ensure we are handling the base case where one of the str is empty.

class TabSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            m, n = len(text1), len(text2)
            dp = [[0]* (n+1) for _ in range(m+1)]

            #Below check is unnecessary as it is the case
            # where both strings are empty (i.e., the base case).
            # if text1[0] == text2[0]:
            #     dp[0][0] = 1

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[m][n]

    def sp_opt_longestCommonSubsequence(self, text1: str, text2: str) -> int:
            m, n = len(text1), len(text2)
            prev = [0]* (n+1)


            for i in range(1, m + 1):
                curr = [0]* (n+1)
                for j in range(1, n + 1):
                    if text1[i - 1] == text2[j - 1]:
                        curr[j] = 1 +prev[j - 1]
                    else:
                        curr[j] = max(prev[j], curr[j - 1])
                prev = curr

            return prev[n]


# TC: O(M∗N)
# SC: O(MxN) , SC: O(N)
