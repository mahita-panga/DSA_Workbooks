"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

HEAP+SLiding window
"""

import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        res = []
        maxheap = []

        # Build initial max heap for the first window
        for i in range(k):
            heapq.heappush(maxheap, (-nums[i], i))  # Store (value, index)

        res.append(-maxheap[0][0])  # Get the maximum for the first window

        for i in range(k, len(nums)):
            # Remove elements not in the window
            while maxheap and maxheap[0][1] <= i - k:
                heapq.heappop(maxheap)

            # Add the new element in the current window
            heapq.heappush(maxheap, (-nums[i], i))

            # The current max is the root of the heap
            res.append(-maxheap[0][0])

        return res
