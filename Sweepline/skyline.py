"""
https://leetcode.com/problems/the-skyline-problem/description/
We need to generate the skyline by identifying the highest points at each building’s start ('st') and end ('e') points

For each building, we generate 2 events -start and end i.e. when building starts it could potentially help
me in creating skyline and when it ends, we need to remove from the consideration

Now, sort the buildings on x-axis:
    You sort events by x-coordinate (leftmost position first).
	•	To handle ties where buildings start and end at the same x-coordinate, sort with a second key:
	•	For start events ('st'), sort in descending height (-h) to prioritize taller buildings.
	•	For end events ('e'), sort in ascending height (h) to remove lower buildings before taller ones.

A max heap keeps track of building heights, where only the tallest building affects the skyline.
->	When a building starts, you add its height to the heap.
->  When a building ends, you remove its height, which updates the skyline if it was the tallest.

"""
from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings_map_xy = []
        for x,y,h in buildings:
            buildings_map_xy.append((x,h,'st'))
            buildings_map_xy.append((y,h,'e'))

        buildings_map_xy = sorted(buildings_map_xy,key=lambda x:(x[0],-x[1] if x[2]=='st' else x[1]))
        print(buildings_map_xy)

        max_heap = [0]
        last_max_height = 0
        output = []
        for bmap in buildings_map_xy:
            x,y,status = bmap[0],bmap[1],bmap[2]
            if status=='st':
                heapq.heappush(max_heap, -y)
            else:
                #the building is ending, then remove the building with its height from the heap
                max_heap.remove(-y)
                heapq.heapify(max_heap)

            current_max_height = -max_heap[0] if max_heap else 0

            # If the max height changes, update the result
            if current_max_height != last_max_height:
                output.append([x, current_max_height])
                last_max_height = current_max_height

        return output
# Sorting events is O(n log n), and heap operations are also O(log n),
# NOTE:  Python’s heapq not directly supporting removal, remove(-h) and heappop(max_heap) clean up the heap after deletions.

#OTHER APPROACH TO SOLVE IS SEGMENT TREES
