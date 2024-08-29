"""
583. Delete Operation for Two Strings

Once we find lcs,
formula should be (m - dp[m][n]) + (n - dp[m][n]).
	•	m - dp[m][n]: Deletions needed to make text1 match the LCS.
	•	n - dp[m][n]: Deletions needed to make text2 match the LCS.
	•	The sum of these values gives the total number of deletions required to make text1 and text2 identical.

"""
class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]* (n+1) for _ in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is the number of deletions required to make both strings identical
        return (m - dp[m][n]) + (n - dp[m][n])
