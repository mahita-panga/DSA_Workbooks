"""
LC #542: 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Intuition:
    -> As we will need to explore the nodes with their nearest neighbours and fill the distance,
    BFS would be best suited which explores the nodes layer by layer

    -> We need to traverse in all 4 directions for all non-zero nodes and identify the distance.
    -> To ensure we are not calculating distance again and again, we can have the distance to nearest zero in the queue.

    -> we will traverse the matrix and put all 0's into the queue with their index, and distance as 0. i.e ([i,j],distance)
    -> Have a visited matrix which identifies if the node is visited or not
    -> Have a distance matrix which will save the distances to nearest 0's

    -> Until the queue is empty:
        -> pop the queue [x,y],distance into x,y and step
        -> update distance matrix with this distance
        -> for all 4 directions:
            -> if the indexes are in bounds and if it is not visited (i.e it does not have 0):
                mark it visited.
                distance is step+1 since it is one step further from the current step to the nearest 0.
                push the new indexes and distance to queue.
"""
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque()
        #queue should hold the number of steps to nearest 0

        visited = [[0 for col in range(n)] for row in range(m)]
        #visited matrix
        distance = [[0 for col in range(n)] for row in range(m)]
        #distance matric

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j]==0:
                    q.append(([i,j],0))
                    visited[i][j] = 1



        while len(q)!=0:
            [x,y],step = q.popleft()
            distance[x][y] = step

            for dx,dy in directions:
                nx = x+dx
                ny = y+dy
                if 0<=nx<m and 0<=ny<n and visited[nx][ny]!=1:
                    visited[nx][ny] = 1
                    q.append(([nx,ny],step+1))

        return distance


mat = [[0,0,0],[0,1,0],[1,1,1]]
Solution().updateMatrix(mat)

"""
Time Complexity: O(NxM + NxMx4) ~ O(N x M)
For the worst case, the BFS function will be called for (N x M) nodes, and for every node, we are traversing for 4 neighbors, so it will take O(N x M x 4) time.

Space Complexity: O(N x M) + O(N x M) + O(N x M) ~ O(N x M)
O(N x M) for the visited array, distance matrix, and queue space takes up N x M locations at max.
"""
