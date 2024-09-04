"""
1092. Shortest Common Supersequence

Intuition:
    -> Find LCS of two strings : this is for dp table construction
    -> Print the LCS of string by backtracking the dp table.
    -> While printing:
        ensure that when s[i]==t[j], print/append the element once
        and when not equal, whichever direction we are taking append that element

        Once either i/j are exhausted, print all the remaining chars in whatever str left
    -> Since we traverse the dp table from bottom, we need to reverse.

TC: O(mxn) SC: O(mxn)
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        def lcs(i,j,s,t):
            m,n=len(s),len(t)
            dp = [[0]*(n+1) for _ in range(m+1)]

            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s[i-1] == t[j-1]:
                        dp[i][j] = 1+ dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp

        dp = lcs(len(str1),len(str2),str1,str2)

        lcs = []
        i, j = len(str1), len(str2)
        while i > 0 and j > 0:

            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
            else:
                lcs.append(str2[j - 1])
                j -= 1

        while i > 0:
            lcs.append(str1[i - 1])
            i -= 1
        while j > 0:
            lcs.append(str2[j - 1])
            j -= 1

        lcs.reverse()
        return ''.join(lcs)
