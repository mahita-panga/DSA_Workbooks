"""
LC #200: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
--> Directions are given as 4, if given diagonals too, we need to consider 8

Intuition:
    -> We can do BFS/DFS traversal to identify the number of islands.
    -> We need to do BFS traversal for every base 1 that we see in the grid and find all its connected components
       The base 1 along with connected components is 1 island
       -> For this case we define a traversal method which will traverse all the connected 1's in the grid and
       mark them visited
       -> We have a visited matrix which helps us traverse only unvisited islands
       -> we traverse the grid and if grid[i][j] == "1"  and this is not visited:
           then run the traversal over this.
       -> Num of times the traversal method is called is the number of islands.

"""
from collections import deque
from typing import List
class Solution:
    def traversal(self, i,j,visited,grid):
        q = deque()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m= len(grid)
        n = len(grid[0])

        q.append((i,j))
        visited[i][j] = 1

        while len(q) !=0 :
            i,j = q.popleft()
            for dx,dy in directions:
                nx = i+dx
                ny = j+dy
                if 0<=nx<m and 0<=ny<n and visited[nx][ny] == 0 and grid[nx][ny]=='1': #Made a mistake of wrong comparision..Grid elements are strings, not integers!!
                    q.append((nx,ny))
                    visited[nx][ny] = 1

    def numIslands(self, grid: List[List[str]]) -> int:
        m= len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j] == 0:
                    cnt+=1
                    self.traversal(i,j,visited,grid)

        return cnt

"""
Time complexity:
    O(N*M + 4*N*M)
Space:
    O(N*M + N*M) ->visited array and queue.
"""
