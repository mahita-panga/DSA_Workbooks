"""
https://leetcode.com/problems/house-robber/

MAXIMUM SUM OF NON-ADJACENT ELEMENTS:
    INTUITION:
        - Recursion :
            Since we need to identify the non-adjacent subsequent elements and find max sum,
            we can choose the pick/no-pick idea of choosing elements recursively.

            PICK: if we choose to pick curr_element, then the choice is : add curr element to sum
            + pick element at index-2 //NO ADJACENT ELEMEMTS

            NO_PICK: if we choose not to pick curr_element, then the choice is: add 0 (as we have not choosen)+
            pick element at index-1 //SINCE WE HAVE NOT CHOOSEN CURR INDEX

            MAXIMUM(PICK,NO_PICK) is the solution.

        a quick trace: [1,2,4,9]
                        0 1 2 3

        f(3):0+ NP -> max(2,5) f(2) : 0+ NP -> f(1) returns 2
                                    : 4+ P  -> f(0) returns 1
            :9 + P  -> max(2,0) f(1) NP -> f(1) returns 2+0
                                 P  -> f(-1) returns 0
        MAX(11,5) = 11 : ANSWER

        Memoization:
            Create a dp array, save the subproblems which are already seen
        Tabulation:
            To save on the extra recursion stack space, we can go bottom up
            In bottom up, we first identify base cases and save them to variables
            and then go up to identify the answer.
            Edge case: handle if arr has 0/1 elements
            base cases : prev2 = arr[0], prev1 = max(arr[0],arr[1])
            Solving:
                keep updating prev2 and prev1 as move bottom up with the values we get
                i.e. prev1 should contain the max of pick/non-pick until the curr ele
                and prev2 will contain max until prev ele.

"""


class Solution:
    def max_sum(self,index,nums):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        pick = nums[index] + self.max_sum(index-2,nums)
        not_pick = 0 + self.max_sum(index-1,nums)
        return max(pick,not_pick)

    def rob(self, nums: List[int]) -> int:
        return self.max_sum(len(nums)-1,nums)


## MEMOIZATION
class Solution:
    @cache
    def max_sum(self,index,nums):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        pick = nums[index] + self.max_sum(index-2,nums)
        not_pick = 0 + self.max_sum(index-1,nums)
        return max(pick,not_pick)

    def rob(self, nums: List[int]) -> int:
        return self.max_sum(len(nums)-1,tuple(nums))


##MEMOIZATION WITH DP_ARRAY:
class Solution:

    def max_sum(self,index,nums,dp):
        if dp[index]!= -1:
            return dp[index]
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        pick = nums[index] + self.max_sum(index-2,nums,dp)
        not_pick = 0 + self.max_sum(index-1,nums,dp)
        dp[index] = max(pick,not_pick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.max_sum(len(nums)-1,nums,dp)


##TABULATION

class Solution:
    def max_sum(self,nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0],nums[1])

        for i in range(2,n):
            pick = nums[i] + prev2
            no_pick = 0 + prev1
            curr_i = max(pick,no_pick)
            prev2 = prev1
            prev1 = curr_i
        return prev1

    def rob(self, nums: List[int]) -> int:
        return self.max_sum(nums)
