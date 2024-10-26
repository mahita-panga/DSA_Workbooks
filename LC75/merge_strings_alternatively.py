"""
LC1768
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Intuition:
    Just iterate over the stringgs and add to the result.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i,j = 0,0
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                res+=word1[i]
                i+=1
            if j<len(word2):
                res+=word2[j]
                j+=1
        return res

#CONCISE SOLUTION
class ConcSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]
        if len(word2) > len(word1):
            res += word2[len(word1):]
        elif len(word1) > len(word2):
            res += word1[len(word2):]

        return res
