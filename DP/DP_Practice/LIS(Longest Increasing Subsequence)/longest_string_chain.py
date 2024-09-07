"""
1048. Longest String Chain

-> Similar to finding LIS.
Only change is that we have to find if the word differs by only 1 character.
Then it means it is part of string chain.

"""
class Solution:
    #METHOD TO CHECK IF THE STRINGS DIFFER BY 1 WORD
    def can_form(self, shorter: str, longer: str) -> bool:
        # Check if `shorter` can be formed by removing one character from `longer`
        if len(longer) - len(shorter) != 1:
            return False

        i, j = 0, 0
        mismatch = 0
        while i < len(shorter) and j < len(longer):
            if shorter[i] == longer[j]:
                i += 1
            else:
                mismatch += 1
                if mismatch > 1:
                    return False

            j += 1
        # Return True if shorter fits into longer with one character removed
        return i == len(shorter)

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        dp = [1]*len(words)
        for i in range(1,len(words)):
            for j in range(i):
                if self.can_form(words[j],words[i]):
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)
