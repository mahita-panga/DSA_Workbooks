"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.


Soln:
    max heapify the array
    take top two ele and smash together. push the remaining weight if >0 back to heap
    do until heap has only 1 ele.
    if heap has 0 ele, return 0 else the weight left

"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            x1 = -1*heapq.heappop(max_heap)
            x2 = -1*heapq.heappop(max_heap)

            new_wt = x2-x1 if x1 <= x2 else x1-x2
            if new_wt != 0:
                heapq.heappush(max_heap,-new_wt)

        return -1*max_heap[0] if len(max_heap)>0 else 0
