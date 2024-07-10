"""
LC #994 : Rotting Oranges:
    You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Intuition:
 Use BFS to identify neighbours to rot and every time we are rotting, we increment the timer.
-> Identify total_oranges in the grid
-> Push the indexes of all rotten oranges into a queue
-> Initialize rotten_oranges = len(queue_of_rotten_oranges)
-> Until the queue is empty:
    pop a rotten orange index,
    fetch the neighbours (top,bottom,left,right) using directions = [(1,0),(-1,0),(0,1),(0,-1)].
    for all neighbours:
        x-axis should always be >=0 and < leng(grid) #m and y-axis should be >=0 and <len(grid[0]) #n
        if the orange in this grid position is fresh, rot it, add it to queue and increment the rotten_oranges

    Increment the timer
-> if total_oranges == rotten_oranges i.e all oranges are rotten: return timer - 1,
since we did increase the time after all the oranges are rotten
-> else return -1 i.e few fresh oranges are still left.

"""
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_oranges = 0
        rotten_q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] ==2: #Its a rotten orange
                    rotten_q.appendleft([i,j])
                    total_oranges+=1
                if grid[i][j] ==1: #Fresh orange
                    total_oranges+=1

        minutes = 0
        if total_oranges == 0:
            return 0
        rotten_oranges = len(rotten_q)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while len(rotten_q)!=0:
            for _ in range(len(rotten_q)):
                rotten_orange_pos = rotten_q.pop()
                i = rotten_orange_pos[0]
                j = rotten_orange_pos[1]


                for x,y in directions:
                    nx = i+x
                    ny = j+y
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]):
                        if grid[nx][ny] == 2 or grid[nx][ny] == 0:
                            continue
                        if grid[nx][ny] == 1:
                            rotten_q.appendleft([nx,ny])
                            rotten_oranges +=1
                            grid[nx][ny] = 2


            minutes +=1

        if rotten_oranges == total_oranges:
            return minutes -1
        else:
            return -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))
