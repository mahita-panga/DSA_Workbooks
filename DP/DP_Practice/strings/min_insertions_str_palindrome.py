"""
LC 1312:  Minimum Insertion Steps to Make a String Palindrome


Min insertions required to make a string palindrome is
-> to identify which subsequence makes a palindrome
-> We just need to insert the remaining characters which are not palindrome to make it palindrome
Question asks us to identify number of insertions:
    Hence ans -> len(s) - longest palindromic subseq length.
"""

class Solution:
    def minInsertions(self, s: str) -> int:
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


        return len(s) - dp[m][n]
