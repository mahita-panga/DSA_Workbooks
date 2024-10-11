"""
Get kth largest element in array.

Best way to do it: Use MAX HEAP
TC: Heapify : O(n) < where n is the length of heaps
    Pop operations: O(klogn) for k elements
Total: O(n+klogn)
SC: O(n)

Normal sort action: O(nlogn)+O(1)// to access kth element.
When k is small, heap is the best approach!
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap) #Need to create a max heap
        for i in range(k-1):
            heapq.heappop(max_heap)
        return -max_heap[0]
