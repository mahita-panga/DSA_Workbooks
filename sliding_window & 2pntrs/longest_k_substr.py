"""
https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

Intuition:
    *   Use sliding window to dynamically track valid substrings.
	•	Use Counter to maintain frequency of characters in the window.
	•	Shrink the window from the left when the number of distinct characters exceeds k.
	•	Track max length when the window has exactly k distinct characters.
"""
from collections import Counter
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n=len(s)
        l=0
        cntr_map = Counter()
        max_len = -1
        for r in range(n):
            cntr_map[s[r]] += 1

            # Shrink window if distinct chars exceed k
            while len(cntr_map) > k:
                cntr_map[s[l]] -= 1
                if cntr_map[s[l]] == 0:
                    del cntr_map[s[l]]
                l += 1

            # Check if current window is valid
            if len(cntr_map) == k:
                max_len = max(max_len, r - l + 1)

        return max_len
