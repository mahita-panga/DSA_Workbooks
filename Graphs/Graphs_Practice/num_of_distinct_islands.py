"""
GFG: https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1

Similiar to num_of_islands, in this we need to identify the number of distinct islands.
Intuition:
    -> As we are doing the bfs traversal, we will identify the connected 1's co-ordinates and add to the list
    -> Once we complete traversal for one path, we will have the base and it connected components in an array
    -> We need to identify the number of distinct islands in this result which is done as:
        -> Consider a set which will save the shape of the island.
        -> for every path in the list, identify the shape i.e. connected(i,j) - base(i,j).
    ->Return len(set)

NOTE: Ensure that only hashable type should be added to the set. Convert list to tuple or json string.

"""
from collections import deque
class Solution:
    def traversal(self, i,j,visited,grid,res):
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
                    res.append((nx,ny))
        return res

    def find_base_shape(self,arr):
        base = arr[0]
        res = []
        for i in range(0,len(arr)):
            res.append((arr[i][0] - base[0], arr[i][1] - base[1]))
        return tuple(res) #since list is unhashable and cannot be directly added to a set. Converting it to tuple




    def numDistinctIslands(self, grid: List[List[str]]) -> int:
        m= len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]

        distinct_islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j] == 0:
                    res = [(i,j)]
                    self.traversal(i,j,visited,grid,res)
                    distinct_islands.add(self.find_base_shape(res))

        return len(distinct_islands)


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","1"],
  ["0","0","0","1","1"]
]
Solution().numDistinctIslands(grid)
