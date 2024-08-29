"""
LENGTH OF LONGEST COMMON SUBSTRING

ONLY thing is when the str match is not there, we can have dp table values as 0.
When match is there add 1 and compare its diagonal.

Recursion needs us to keep a track of chars to visit. So we are using the tabulation of lcs
and tweaking it for our use.

"""

class Solution:
    def longestCommonSubstr(self, text1, text2):
        # code here
        m, n = len(text1), len(text2)
        dp = [[0]* (n+1) for _ in range(m+1)]

        #Below check is unnecessary as it is the case
        # where both strings are empty (i.e., the base case).
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
                res = max(dp[i][j], res)

        return res
