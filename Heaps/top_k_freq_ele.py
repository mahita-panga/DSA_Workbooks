"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

-> counter of array
-> max heapify the counter based on its counts
-> get top k counts and their corresponding vals into a res

"""

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        max_heap = [(-x[1],x[0]) for x in cntr.items()]
        heapq.heapify(max_heap)
        res = []
        for i in range(k):
            cnt,val = heapq.heappop(max_heap)
            res.append(val)
        return res
