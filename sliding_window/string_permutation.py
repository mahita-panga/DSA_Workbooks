"""
Given two strings s1 and s2, return true if s2 contains a
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Intuition:
    Bruteforce is use nested loops to check each and every possible subarray of len(s1)
    and keep comparing. This will give TLE. TC O((n - m + 1)* m log m) , sorting each subarray and comparing.


    Instead, we can use sliding window technique.
    We know the window size which is len(s1).
    To keep track of the characters, we can use a map to maintain character frequencies of s1 and s2(window length).
    In whichever window, if we see that the character frq table matches,
    we return True else continue till the end.

    -> sliding window will loop until, len(s2)-len(s1).


"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Cntr = [0]*26
        s2Cntr = [0]*26

        for i in range(len(s1)):
            s1Cntr[ord(s1[i])-ord('a')] +=1
            s2Cntr[ord(s2[i])-ord('a')] +=1 #Initial window calculation for s2

        #slide a window of length s1 over s2.
        for i in range(len(s2)-len(s1)): #iterate until the last but 1 window range
            if s1Cntr == s2Cntr:
                return True
            s2Cntr[ord(s2[i]) - ord('a')] -= 1 #Removing leftmost character in the window.
            s2Cntr[ord(s2[i+len(s1)])-ord('a')] +=1 #Adding the next character in the window

        return s1Cntr == s2Cntr
