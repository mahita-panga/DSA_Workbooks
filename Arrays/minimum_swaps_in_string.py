"""
Why +1 in umatched_close+1//2:
Every unmatched_closing bracket needs a swap with open bracket.
every 2 unmatched_closing brackets can be corrected with 1 swap: ]] -> []
1 remaining unmatched in case of odd unmatched brackets will also be needing 1 swap. So formula: n+1//2


"""
class Solution:
    def minSwaps(self, s: str) -> int:
        umatched_close = 0
        cnt_open = 0
        swaps = 0
        for char in s:
            if char == '[':
                cnt_open+=1
            if char == ']':
                if cnt_open ==0:
                    umatched_close +=1
                else:
                    cnt_open-=1
        swaps = (umatched_close+1)//2
        return swaps
