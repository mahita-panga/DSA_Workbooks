"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Use a monotonic increasing stack to keep track of bars.
When a shorter bar is found, it means
the taller bars in the stack can’t extend further → compute area.

	•	stack = [-1] handles width cleanly even when stack becomes empty.
	•	On popping: area  = height * (i - stack[-1] - 1).
	    Here width at any i is calculated as
					right_boundary(number of bars < this bar) - left_boundary(number of bars < this bar)  +1
					(i-1) - (stack[-1]+1 )+1  = i-(stack[-1]) -1
	•	Append a 0-height bar at the end to flush the remaining stack in one loop.

heights = [2, 1, 5, 6, 2, 3]
1.	Push 2 → then pop when 1(1<2) arrives → area = 2 × 1 = 2
2.	Push 1 → push 5(5>1), push 6(6>5) → pop 6, pop 5 when 2 arrives as 5 and 5 are >2
    → area = 6×1=6,
          =  5×2=10
3.	Remaining pops give 2×4=8, 1×6=6

"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Add a right boundary height of 0 to flush the stack
        stack = [-1]  #initially -1 to avoid stack boundary checks !! SMART WAY to avoid if stack check and also if stack gets empty then
        #width = i- (-1)-1 = i

        max_area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
