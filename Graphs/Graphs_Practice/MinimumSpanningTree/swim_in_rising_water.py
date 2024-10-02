"""
LC 778: Swim in Rising Water
We can move up, down, left, or right, but
 we can only step on cells with elevations less than or equal to the current time.
The goal is to find the minimum “time” such that you can reach the bottom-right corner from the top-left corner of the grid.

Approach:
    We can leverage Disjoint set here. Idea for Union find is, we can track the connectivity
    as time progresses and once we identify that source(0,0) and destination(n-1,n-1) are
    connected, it means we have found the earliest time it takes.

Intuition:
    Initially we will have less cells to access but as time progresses we will have more cells to
    access and we will be forming a path as time moves on. The first path that forms is the minimal time
    and hence we can return the time.

    We are continously connecting neighbouring nodes with the time if their elevation is <= time.

BUT BEST APPROACH HERE IS MODIFIED DIJKSTRA's:
    Reason - We are processing each cell one by one  in terms of time which is redundant
    We can use Priority queue to prioritize the cells with lower elevations and explore them directly using Dijkstra's

    -> In this algorithm, instead of using current elevation, we will keep track of the max elevation in curr path.
    -> We will explore the paths with min. max elevation :D

TC: O(n² * α(N))
SC: O(n²)

DIJKSTRA'S -> Similar to minimum path effort.
- This follows the principle of “least elevation first,” rather than working through all elevations for all cells as Union-Find does.
TC: O(n² * log(n²)): You process each of the n*n cells, and each time you pop from the heap or push to the heap, it takes O(log(n²)) time.


"""
from typing import List
#UNION FIND:
class Disjoint_Set:
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.size = [1] * (N+1)

    def get_parent(self):
        return self.parent

    def findUP(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUP(self.parent[node])  # Path compression
        return self.parent[node]

    # Union by Size
    def UnionBySize(self, u, v):
        pu = self.findUP(u)
        pv = self.findUP(v)

        if pu != pv:  # They are in different sets
            # Attach the smaller tree under the larger tree
            if self.size[pu] < self.size[pv]:
                self.parent[pu] = pv  # Attach u's root to v's root
                self.size[pv] += self.size[pu]  # Update size of v's root
            else:
                self.parent[pv] = pu  # Attach v's root to u's root
                self.size[pu] += self.size[pv]  # Update size of u's root


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = Disjoint_Set(n*n)

        time_map = {}
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(n):
                time_map[grid[i][j]] = (i,j) #This map will help us tell the i,j we can be at time t

        for time in range(n*n):
            x,y = time_map[time]
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny] <= time:
                    ds.UnionBySize(grid[x][y], grid[nx][ny])

            if ds.findUP(grid[0][0]) == ds.findUP(grid[-1][-1]):
                return time
        return -1


#DIJKSTRA's
import heapq

class Dij_Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0]*n for _ in range(n)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pq = [(grid[0][0],0,0)]
        time = grid[0][0]
        visited[0][0] = 1
        while pq:
            time,row,col = heapq.heappop(pq)
            if row==n-1 and col==n-1:
                return time
            for dx,dy in directions:
                nx = dx+row
                ny = dy+col
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]!=1:
                    visited[nx][ny] = 1
                    heapq.heappush(pq,(max(time,grid[nx][ny]),nx,ny))
        return -1
