"""
LC 78. Subsets

Given an integer array nums of unique elements, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Solving this via recursion
-> Base case:
    Append the current array which contains one of the subsequence to the res
    return <- this backtracks on the recursion tree
For generating the subsequence, take arr :
    -> add all the elements of the list one by one
    -> remove elements of the list one by one

"""

class Solution:
    def recursion(self,i,arr,nums,res):
        if i==len(nums):
            res.append(arr.copy())
            return
        arr.append(nums[i])
        self.recursion(i+1,arr,nums,res)
        arr.pop()
        self.recursion(i+1,arr,nums,res)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.recursion(0,[],nums,res)
        return res
