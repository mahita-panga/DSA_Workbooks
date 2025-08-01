"""
Given a string s, find the length of the longest substring without duplicate characters.


Soln -
 sliding window with two pointers to track a unique substring. Expand the right pointer to include new characters and shrink from the left whenever a duplicate is found, always recording the maximum window size
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_set = set()
        left = 0
        max_cnt = 0

        for right in range(len(s)):
            # If duplicate, shrink from the left
            while s[right] in chr_set:
                chr_set.remove(s[left])
                left += 1
            # Add current character and update max length
            chr_set.add(s[right])
            max_cnt = max(max_cnt, right - left + 1)

        return max_cnt

#REVISION
class RevSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_set = set()
        left = 0
        right = 0
        max_cnt = 0
        cnt = 0
        while right<len(s):
            if s[right] in chr_set:
                chr_set.remove(s[left])
                left+=1
                cnt -=1
            else:
                chr_set.add(s[right])
                right+=1
                cnt+=1
            max_cnt = max(max_cnt,cnt)
        return max_cnt
