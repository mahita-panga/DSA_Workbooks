"""
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/

BASED On mistakes while submitting this, ensure:
    --- Don’t fix k as the number of candies to give each child.
    --- Instead, search for the largest x (candies per child) such that:
    ∑ (candies in each pile) // x ≥ k
       •	If you can serve ≥ k kids with x candies each → try higher x.
	   •	If you can’t, try a smaller x.
"""

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # return sum(candy//k for candy in candies if candy >=k)
        """
        PROBLEM WITH ABOVE APPR: I am looking for a way to distribute m chocolates to k children but problem is each child can get chocolates from one heap only. so we have to find the number of candies we can give to k children and these heaps should be formed from the piles given. i.e ex for:
        [1,2,3,4,10] and k=5 , if we choose pile of size 2
        1//2 - 0, 2//2-1, 3//2-1,4//2-2,10//2-5 =>9 children can get piles of size 2

        -- translates to binary search problem where we choose a pile and see if we can get to k children with that choice. if num of children served >k, then we increase pile size else we decrease.
        - bounds - [0,max(candies) available]
        """

        l, r = 1, max(candies) + 1
        ans = 0
        while l < r:
            mid = (l + r) // 2
            if sum(candy // mid for candy in candies) >=k:
                ans = mid
                l = mid + 1
            else:
                r = mid
        return ans
