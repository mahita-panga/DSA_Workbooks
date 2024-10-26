"""
Intuition of using Segment Tree:
    -> We are having 2 things :
       	1.	Range Updates: Each building affects a range on the x-axis (from left to right with a certain height).
        2.	Range Queries: We need to check the maximum height at different x-coordinates to determine the outline.
	Seg tree is ideal for faster range queries and efficient updates

NOTE: A new thinking in this is Co-ordinate compression:
    Due to potentially large values of x-coordinates, we use coordinate compression. This helps us map the x-coordinates to a smaller range, optimizing the segment tree’s space requirements and performance.

Actions in this problem:
    Coordinate Compression:
	•	We extract and sort all unique x-coordinates, compressing them into a smaller, sequential range.
	•	This reduces the need for a large segment tree array and optimizes updates and queries.
	Segment Tree Setup:
	   - initialize segtree
       - For each building, update the segment tree using the compressed co-ordinates for building's original
    	co-orfdinates. The segment tree will store the maximum height within each range, allowing it to handle overlapping buildings correctly.

	Generating the Skyline with Range Queries:
		•	Traverse the compressed x-coordinates and query the segment tree at each step.
		•	If the height at the current x-coordinate differs from the last height, it represents a change in the skyline, so we record this point.

"""

class SegTree:
    def __init__(self,n):
        self.size = n
        self.segTree = [0]*2*n

    def update_range(self,left,right,val):
        left += self.size
        right += self.size
        while left<right:
            if left&1: #If left is an odd index, it means that st[left] fully covers part of the range we’re querying.
                self.segTree[left] = max(self.segTree[left],val)
                left+=1
            if right&1:
                right-=1
                self.segTree[right] = max(self.segTree[right],val)
            #move left and right to their respective parent nodes
            left >>= 1
            right >>= 1

    def query(self,pos):
        pos += self.size
        height = 0
        while pos>0:
            height = max(height,self.segTree[pos])
            pos>>=1
        return height

from typing import List
from collections import deque

class Solution:
    def heapgetSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
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
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings_map_xy = []
        for x,y,h in buildings:
            buildings_map_xy.append((x,h,'st'))
            buildings_map_xy.append((y,h,'e'))

        #seg tree works on contigous elements, so take the x and y co-ordinates and create a seg tree
        coords = set()
        for x,y,_ in buildings:
            coords.add(x)
            coords.add(y)
        coords = sorted(coords)
        #We can do co-ordinate compression which will help us map the large co-ordinate values to the map
        compressed_coords = {v:i for i,v in enumerate(coords)}
        #This will ensure all the large co-ordinates are mapped based on their index values i.e smaller index will be mapped to smaller coordinates and larger i for large coords
        segTree = SegTree(len(compressed_coords))
        # Update segment tree with each building
        for left, right, height in buildings:
            segTree.update_range(compressed_coords[left], compressed_coords[right], height) #Add each building with their respective co-ord into segtree

        res = []
        last_max_height = 0

        # Build the skyline by querying each coordinate
        output = []
        last_height = 0
        for x in coords:#sorted coords, check for each co-ordinate
            current_height = segTree.query(compressed_coords[x])
            if current_height != last_height:
                output.append([x, current_height])
                last_height = current_height

        return output
"""
TC: Co-ordinate compression: O(mlogm) m is number of unique coordinates
    Mapping co-ord to index: O(m)
    Building seg tree: O(logm) for each building, So O(nlogm) <-n buildings
    Querying for the skyline: O(mlogm) <- m unique co-ords and each co-ord query to fetch max height: O(logm)
    Total: O(m+mlogm+nlogm+mlogm)
    ~= O((m+n)logm)

SC: O(2m(segtree)+m(map)) ~ O(m)
"""
