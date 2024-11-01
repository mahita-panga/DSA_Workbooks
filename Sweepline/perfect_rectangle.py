"""
LC 391. Perfect Rectangle
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.


"""
#Sweepline technique
#Total area covered == bounding area rectangle + NO Overlaps
#Bounding Area: x1min,y1min, x2max,y2max

#Event Identification
#Event Sorting
#Query Sorting
#Active Set
#Event Processing
#Calc as required
from sortedcontainers import SortedList
from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        events = []
        tot_rec_area = 0
        for x1,y1,x2,y2 in rectangles:
            events.append((x1,y1,y2,'start'))
            events.append((x2,y1,y2,'end'))
            tot_rec_area += (x2-x1)*(y2-y1)

        events.sort(key=lambda x:(x[0],x[3]=='start')) #sort by x axis

        #Bounding Area Identification
        x1min = min(x[0] for x in rectangles)
        y1min = min(x[1] for x in rectangles)
        x2max = max(x[2] for x in rectangles)
        y2max = max(x[3] for x in rectangles)

        bounding_area = (x2max-x1min)*(y2max-y1min)
        prev_x = None
        #Direct check if tot_area is not equal to bounding_area
        if tot_rec_area != bounding_area:
            return False

        #Sweepline processing for overlaps
        active_intervals = SortedList()

        for x,y1,y2,event in events:
            # Only check coverage when moving to a new x-coordinate
            if prev_x is not None and x != prev_x and len(active_intervals)>0:
                #if intervals are not fully covered by the y range i.e. gaps are there then return False
                if not self.range_check_y(active_intervals, y1min, y2max):
                    return False
                prev_x = x

            if event=='start': #means adding a new interval
                #before adding any new interval, check if it overlaps with the y interval
                active_intervals.add((y1,y2))
            elif event=='end':
                active_intervals.remove((y1,y2))

            prev_x = x

        return True

    def range_check_y(self,active_intervals,y1min,y2max):
        #Check if intervals cover the y-range [y1min, y2max] exactly without gaps
        current_y = y1min
        # print(active_intervals)
        if active_intervals:
            for y1, y2 in active_intervals:
                # There should be no gap between current_y and the start of this interval
                if y1 != current_y:
                    return False
                # Move the current_y forward by the length of the interval
                current_y = y2

        # After processing all intervals, current_y should exactly match y2max
        # print(f'{current_y} and {y2max}')
        return current_y == y2max

#TC: Event Creation: O(N), Sorting: O(NlogN), Sweeoline O(N), active set: add/del: O(logN) Range Check: O(N) so total O(NlogN)
#SC: O(N)


#O(N) approach - Mathematical way
"""
Approach:
    first calculate the total area of all the rectangles and store their corners in a set. Then, we check if all corners are unique and if the total area is equal to the area of the union rectangle. Finally, we check if the total number of corners is equal to the sum of the areas of the rectangles divided by the area of a single rectangle.
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # calculate the area of all the rectangles
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            # check if each corner is unique
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        # check if all corners are unique
        if len(corners) != 4:
            return False
        # calculate the area of the union rectangle
        x1, y1 = float("inf"), float("inf")
        x2, y2 = float("-inf"), float("-inf")
        for x, y in corners:
            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, x)
            y2 = max(y2, y)
        union_area = (x2 - x1) * (y2 - y1)
        # check if the total area of all the rectangles is equal to the area of the union rectangle
        if area != union_area:
            return False
        # check if the total number of corners is equal to the sum of the areas of the rectangles divided by the area of a single rectangle
        return area == (x2 - x1) * (y2 - y1)
