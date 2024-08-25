"""
LC 494: https://leetcode.com/problems/target-sum/description/
Intuition:
    We have to find number of ways we can achieve the target sum by adding +/- to the numbers
    Since we can recursively add +/- (similiar to pick/not-pick) to all elements of our array and
    see when we reach our target value
    In negative, we have subtract the arr[index] from our curr sum and vice versa

    Catch here is:
        * When calculating the sum in the recursive process, curr_sum can be either positive or negative
        depending on whether we add or subtract elements from the array nums.
        * To avoid negative values, we need to shift the index.by adding sum_all to curr_sum.
		* sum_all is the sum of all elements in nums. By adding sum_all to curr_sum,
	we ensure that all possible values of curr_sum (both negative and positive) are mapped to a valid non-negative index in the dp array.
	    * Using the Shifted Indices which accessing the dp table.
		* To ensure this, we are creating a sp table of size 2*total_sum + 1 (to accomodate both pos and neg)



"""
#Memoization
from typing import List
class Solution:
    def sumWaysUtil(self, index, curr_sum, target, nums, dp, sum_all):
        if index <= 0:
            if curr_sum == target:
                return 1
            return 0

        if dp[index][curr_sum + sum_all] != -1:
            return dp[index][curr_sum + sum_all]

        # Explore both adding and subtracting the current number
        neg = self.sumWaysUtil(index - 1, curr_sum - nums[index], target, nums, dp, sum_all)
        pos = self.sumWaysUtil(index - 1, curr_sum + nums[index], target, nums, dp, sum_all)

        dp[index][curr_sum + sum_all] = neg + pos
        return dp[index][curr_sum + sum_all]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_all = sum(nums)
        dp = [[-1] * (2 * sum_all + 1) for _ in range(len(nums))]

        # Start recursion with the initial sum of 0, considering the shifted index
        return self.sumWaysUtil(len(nums) - 1, 0, target, nums, dp, sum_all)

nums = [1,1,1,1,1]
target = 3
print(Solution().findTargetSumWays(nums,target))

#TABULATION
class TabSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
            sum_all = sum(nums)
            dp = [[0] * (2 * sum_all + 1) for _ in range(len(nums)+1)]

            if abs(target) > sum_all:
                return 0

            dp[0][sum_all] = 1 #Base case: The only possibility of having sum of 0 is by picking no elements

            for i in range(1,len(nums)+1):
                for j in range(-sum_all,sum_all+1):
                    if dp[i-1][j+sum_all] > 0:
                        # neg = dp[i-1][j-nums[i-1]+sum_all]
                        # pos = dp[i-1][j+nums[i-1]+sum_all]
                        # dp[i][j+sum_all] = neg + pos

                        dp[i][j - nums[i - 1] + sum_all] += dp[i - 1][j + sum_all]
                        dp[i][j + nums[i - 1] + sum_all] += dp[i - 1][j + sum_all]

            return dp[len(nums)][target+sum_all]

"""
Reason why commented lines were not working:
    Indexing Issue: It is meant to calculate the number of ways to achieve the sum j after either subtracting or adding the current number nums[i-1].
    However this code did not properly handle the cases where j - nums[i-1] or j + nums[i-1] fell outside the range [-sum_all, sum_all].
Below should be done (GPT notes):
    •	For each element nums[i-1], there are two options:
    	1.	Subtract the Element (-nums[i-1]):
    	•	If you subtract the element from the current sum j, you are effectively reducing the sum. Therefore, the entry dp[i][j - nums[i-1] + sum_all] is updated by adding the number of ways to reach sum j with i-1 elements (dp[i-1][j + sum_all]).
    	2.	Add the Element (+nums[i-1]):
    	•	If you add the element to the current sum j, you are increasing the sum. Thus, the entry dp[i][j + nums[i-1] + sum_all] is updated by adding the number of ways to reach sum j with i-1 elements (dp[i-1][j + sum_all]).
    	3.	Cumulative Update:
    	•	The += operator is used because there may be multiple ways to reach the same sum by different combinations of adding or subtracting elements. Therefore, we accumulate all the possible ways to achieve the sum j.

"""


"""
FAILED CODE : Reason curr_sum can be negative and we can not access negative indexes in Python.
To avoid that we need to use a offset which shifts all the negative sums towards the positive side.

# class Solution:
#     def sumWaysUtil(self,index,curr_sum,target,nums,dp):
#         if dp[index][curr_sum] != -1:
#             return dp[index][curr_sum]

#         if index < 0:
#             if curr_sum == target:
#                 return 1
#             return 0

#         neg =  self.sumWaysUtil(index-1,curr_sum-nums[index],target,nums,dp)
#         pos =  self.sumWaysUtil(index-1,curr_sum+nums[index],target,nums,dp)

#         dp[index][target] = neg + pos
#         return dp[index][target]

#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         sum_all = sum(nums)
#         dp = [[-1]*(2*sum_all+1) for _ in range(len(nums))]
#         return self.sumWaysUtil(len(nums)-1,0,target,nums,dp)
"""
