"""
1631. Path With Minimum Effort
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Intuition:
    -> Need to find the minimum effort -> Dijkstra's.
    -> Effort can be considered as the weights
    -> For every new node, calculate the effort which is max of abs diff with new cell and curr effort
    -> Push the effort into queue if the new dist/effort is less than the existing distance matrix.

    -> Breaking condition: Once you reach the end cell , return curr_distance since that is the min effort
    for the path explored

"""
from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pq = [(0,0,0)]
        distance[0][0] = 0
        abs_sum = 0
        while pq:
            curr_dis, curr_x, curr_y = heapq.heappop(pq)
            if curr_x == m-1 and curr_y == n-1:
                return curr_dis
            for dx,dy in directions:
                nx = dx+curr_x
                ny = dy+curr_y
                if 0<=nx<m and 0<=ny<n:
                    new_dist = max(abs(heights[curr_x][curr_y]-heights[nx][ny]),curr_dis) #Should be the max effort
                    if new_dist < distance[nx][ny]:
                        distance[nx][ny] = new_dist
                        heapq.heappush(pq,(new_dist,nx,ny))

        return 0
