"""
Palindrome: Reverse of the string should match the str
Longest common palindromic sequence:
    LCS of a string and its reverse
    Ex: abbaacba <- s
        abcaabba <- rev(s)
        ---------
    LCS: abaaba  <- This is palindromic and longest. Len: 6
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        m, n = len(s), len(s2)
        dp = [[0]* (n+1) for _ in range(m+1)]

        #Below check is unnecessary as it is the case
        # where both strings are empty (i.e., the base case).
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


        return dp[m][n]
