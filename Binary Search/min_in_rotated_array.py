"""
153. Find Minimum in Rotated Sorted Array

    •	In a rotated sorted array, the minimum element is the only element where the previous element is greater than it.
	•	If nums[mid] > nums[ub], that means rotation has happened after mid, so search in right half.
	•	Else, the minimum is either at mid or in the left half.

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb, ub = 0, len(nums) - 1

        while lb < ub:
            mid = (lb + ub) // 2
            # If mid element is greater than the rightmost, min is in right half
            if nums[mid] > nums[ub]:
                lb = mid + 1
            else:
                ub = mid  # min could be at mid

        return nums[lb]
