"""
295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.


This helps us understand a new concept: Rebalancing 2 heaps.

BRUTEFORCE:
    store all elements in sorted list, each time new ele is added, sort the list and median is middle element
    TC: O(nlogn) for inserting and O(1) for finding median

OPTIMAL: Using Heaps BUT 2 heaps solution
    •	Max-heap (small_heap): Stores the smaller half of the numbers.
	•	Min-heap (large_heap): Stores the larger half of the numbers.
	•	The heaps are balanced such that:
    	•	The size of both heaps differs by at most 1.
    	•	All elements in the max-heap (small_heap) are less than or equal to those in the min-heap (large_heap).
    	•	If the size difference becomes more than 1, rebalance by moving elements between heaps.
    TC: O(logn) for insertions + O(1) for median
"""

import heapq
class MedianFinder:

    def __init__(self):
    #two heaps for finding median,
    #one small_heap which will contain all small numbers
    #one large_heap which will contain all large numbers
    #median will be max(small_heap)+min(small_heap)
    #=> small_heap will be behaving like a max_heap with small numbers and large heap like min_heap.
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        #Rebalancing needs to be done for every insert of element in both heaps
        #Rebalancing condition:
        # abs(len(minHeap)-len(maxHeap))<=1 and max(minHeap)<min(maxHeap)=> both heaps should be approximately equal
        # else rebalance, i.e. pick the max(smallHeap) and push it to large_heap.
        heapq.heappush(self.small_heap,-num)

        if self.small_heap and self.large_heap and -self.small_heap[0]>self.large_heap[0]: #<- rebalancing needed
            val = -1*heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,val)
        #Uneven heap sizes
        #small>large by more than 1
        if len(self.small_heap)-len(self.large_heap)>1:
            val = -1*heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,val)
        #large>small by more than 1
        if len(self.large_heap)-len(self.small_heap)>1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap,-val)


    def findMedian(self) -> float:
        # print(self.small_heap)
        # print(self.large_heap)
        if len(self.large_heap)>len(self.small_heap):
            return self.large_heap[0]
        elif len(self.small_heap)>len(self.large_heap):
            return -self.small_heap[0]
        else:
            return (-1*self.small_heap[0]+self.large_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
