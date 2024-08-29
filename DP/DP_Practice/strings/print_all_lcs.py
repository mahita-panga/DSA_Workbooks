"""
PRINT ALL LCS

DP + Backtracking:
    DP to create the DP table
    Using a stack to backtrack in the dp table
    -> a stack to store the state (i.e., current indices i, j in the DP table and the current LCS string being constructed).
	-> Pop elements from the stack, and explore both directions (up and left) in the DP table to find all possible LCS paths.
	-> If you reach a point where s[i-1] == t[j-1], you append the character to the
	LCS string and continue backtracking from the previous indices (i-1, j-1).

	->	If the values dp[i-1][j] and dp[i][j-1] are the same, you need to push both paths onto the stack to explore both directions.
	-> Continue this process until the stack is empty, and collect all possible LCS strings.

	WAS GETTING TLE.
	To avoid that, we can use memoization for redundant calculations in backtracking.
	 memo = {} is a dict which saves the stack elements as a key. In case this key is found
		no need to calculate but if not found then follow the path.
"""


class Solution:
    def all_longest_common_subsequences(self, s, t):

        m, n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Below check is unnecessary as it is the case
        # where both strings are empty (i.e., the base case).
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        stack = [(m, n, "")]  # Stack stores tuples of (i, j, current_LCS)
        lcs_set = set()

        memo = {}  # For memoization to avoid recomputation

        while stack:
            i, j, current_lcs = stack.pop()

            if (i, j, current_lcs) in memo:
                continue

            memo[(i, j, current_lcs)] = True

            # If we reach the beginning of either string, add the LCS to the set
            if i == 0 or j == 0:
                lcs_set.add(current_lcs)
                continue

            if s[i - 1] == t[j - 1]:
                stack.append((i - 1, j - 1, s[i - 1] + current_lcs))
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    stack.append((i - 1, j, current_lcs))
                if dp[i][j - 1] >= dp[i - 1][j]:
                    stack.append((i, j - 1, current_lcs))

        return sorted(lcs_set)

Solution().all_longest_common_subsequences('abaaa','baabaca')
