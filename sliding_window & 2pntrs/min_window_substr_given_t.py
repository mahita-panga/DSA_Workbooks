"""
Given two strings s and t of lengths m and n
respectively, return the minimum window substring of s such that every character in
t (including duplicates) is included in the window. If there is no such substring, return the empty string "".


Intuition:
        Use a sliding window to expand the right boundary until the window contains all characters from t.
        Then shrink the left boundary to find the smallest possible valid window.
        Use Counter subtraction to efficiently check if the window meets the requirement.

"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window - expand and shrink the window by adding the character from right if the until the cnt reaches len(s2) and check if this potentially is our req substr. if it > len(s2) increase the l counter. do it until end of str and min the len(substr) found
        """

        target_cntr = Counter(t)
        window_cntr = Counter()
        i, j, ans = 0, 0, ""

        while j < len(s):
            while j < len(s) and len(target_cntr - window_cntr) > 0: # expand
                window_cntr[ s[j] ] += 1
                j += 1

            while i < j and len(target_cntr - window_cntr) == 0:    # shrink
                ans = s[i: j] if not ans or j-i < len(ans) else ans
                window_cntr[ s[i] ] -= 1
                i += 1

        return ans
