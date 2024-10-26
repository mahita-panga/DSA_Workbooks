"""
136. Single Number
Given a non-empty array of integers nums,
every element appears twice except for one. Find that single one

Intuition:
    XOR of number with itself gives 0. Xor of number with 0 gives number.
    So, simply do xor of all numbers in the list.

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums[1:]:
            ans = ans^i
        return ans
