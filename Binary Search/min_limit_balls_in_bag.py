"""
1760. Minimum Limit of Balls in a Bag
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.


--- Binary search problem
-- check on the penalty space and see if for this penalty, the operations can be done or not

"""
import math
from typing import List

class Solution:
    def is_possible(self, max_balls,nums,maxOperations):
            tot_operations = 0
            for num in nums:
                operations = math.ceil(num/max_balls) - 1
                tot_operations += operations

                if tot_operations >maxOperations:
                    return False
            return True
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lb = 1
        ub = max(nums)

        while lb < ub:
            mid = (lb+ub)//2
            if self.is_possible(mid,nums,maxOperations):
                ub = mid
            else:
                lb = mid+1

        return lb
