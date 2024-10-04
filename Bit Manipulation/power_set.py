"""
78. Subsets
Given an array, print all possible subsequences.

Intuition:
    This is already solved using recursion.
    we can solve it through bit manipulation as well.
    Lets say we have [1,2,3], possible subsets are [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
    Binary rep of numbers 1 to 2^3: 000,001,010,011,100,101,110,111
    We can use this and whenever there is a 1, pick element at that index.

    So steps are:
        run num through 0,2^n //1<<n in binary rep.
         # check which bits of the num are set. This allows us to choose ele in list
          for i in range(num):
              if num& 1<<i: //checking if the i'th bit is set in the number.
                if yes pick that ele from list.
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for num in range(1<<n): #pow(2,n) == 1<<n
            l = []
            for i in range(n):
                if num & 1<<i: #Check if the ith bit is set.
                    l.append(nums[i])
            res.append(l)
        return res
