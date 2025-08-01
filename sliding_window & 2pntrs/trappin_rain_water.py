"""
https://leetcode.com/problems/trapping-rain-water/

- Water is trapped if there are taller bars on both sides of it.
- The height of water above bar i is: min(max_left, max_right) - height[i]

2 pntrs -
	•   Start from both ends.
	•	Keep track of the max height seen so far from left and right.
	•	Whichever side has smaller max, move that pointer inward — since water trapping depends on the shorter boundary.
	•	For each step, add trapped water = max_so_far - current_height.

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += max(0, right_max - height[right])

        return total_water
