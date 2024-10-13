"""
632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Bruteforce:
    Intuition:
	•	Consider all possible pairs of elements from the lists.
	•	For each pair, check if there is at least one element from each list within the range.
	•	Return the smallest such range.
TC: O(n^k) n - #elements,k- #lists

Optimal Approach (Min Heap and Tracking Max Value): <More like sliding window + heaps
    •	Use a min-heap to track the smallest element across all lists at any point in time.
	•	Simultaneously, track the maximum element seen so far to determine the current range.
	•	The range is determined by the difference between the current smallest element (from the min-heap) and the current maximum element.
	•	Continue expanding the range by adding the next element from the list that had the smallest element, updating the current maximum as needed.
	•	Stop when any list is exhausted, as it’s impossible to cover all lists beyond this point.

•	The min-heap ensures that we always process the smallest available element across lists, while the maximum element is updated to track the largest value within the current range.
•	This structure helps maintain an optimal range that covers elements from all lists.

STEPS:
    •	Push the first element from each list into the min-heap.
	•	Track the maximum element.
	•	Pop the smallest element from the heap, and update the range if the current range is smaller than the previously recorded range.
	•	Push the next element from the same list to the heap and update the maximum if needed.
	•	Continue until one of the lists is exhausted.

TC: Building heap-O(k)
    insertion and pop - O(logk)
    for each ele in the longer list or the list that is being pushed,
    so total TC: (nlogk)
"""

# [4,10,15,24,26] [0,9,12,20] [5,18,22,30] 0, 5
# [4,10,15,24,26] [9,12,20] [5,18,22,30] 4, 9
# [10,15,24,26] [9,12,20] [5,18,22,30] 5, 10
# [10,15,24,26] [9,12,20] [18,22,30] 9, 18
# [10,15,24,26] [12,20] [18,22,30] 10, 18
# [15,24,26] [12,20] [18,22,30] 12, 18
# [24,26] [20] [18,22,30] 18, 24
# [24,26] [20] [22,30] 20, 24
# [24,26] [] [22,30]  stop
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums)==0:
            return []
        min_heap = [] #min heap for each small element of the list
        curr_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap,(nums[i][0],i,0))
            curr_max = max(curr_max,nums[i][0])

        num_range = [float('-inf'),float('inf')]
        while min_heap:
            # print(min_heap)
            # print(num_range)
            curr_min,l_index,ele_index = heapq.heappop(min_heap)
            if curr_max - curr_min < num_range[1]-num_range[0]:
                num_range = [curr_min,curr_max]
            if ele_index + 1 <len(nums[l_index]):
                next_num = nums[l_index][ele_index+1]
                heapq.heappush(min_heap,(next_num,l_index,ele_index+1))
                curr_max = max(curr_max,next_num)
            else:
                break #exhausted one of the list
        return num_range
