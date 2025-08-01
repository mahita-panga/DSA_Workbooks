"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.


->   2 pointers , largest on left and largest on right can possibly store more water
->   move the min of left and right pointers
->   maximize the total water capacity

"""

#Move the smallest pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float('-inf')
        i = 0
        j = len(height)-1
        while i<=j:
            if height[i]<=height[j]:
                area = height[i]*(j-i)
                max_water = max(max_water,area)
                i+=1
            else:
                area = height[j]*(j-i)
                max_water = max(max_water,area)
                j-=1


        return max_water
