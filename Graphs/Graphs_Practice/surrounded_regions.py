"""
LC #130: Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions
that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and
none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Intuition:
    -> One thing for sure is if there is a 'O' in the boundary, then all the connected O's are safe.
    -> Our idea is to find the connected O's in the matrix and mark them safe.

    BFS with - "Queue should have all the safe O's which will not be converted."

    -> For given matrix: first identify all the O's on the border and its connected O's. These will not
    be converted. So mark these as Safe and add them to the queue.

    -> Now perform BFS traversal on the matrix where we traverse all 4 directions and see if we can
    mark any of the O's as Safe.

    -> Flip all the O's to X's and all Safe to O's.
"""
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        q = deque()

        # Function to mark 'O's connected to borders as safe
        def mark_safe(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                q.append((i, j))
                board[i][j] = 'S'

        # Step 1: Mark all border 'O's and their connected 'O's as safe
        for i in range(m):
            mark_safe(i, 0)  # Left border
            mark_safe(i, n - 1)  # Right border
        for j in range(n):
            mark_safe(0, j)  # Top border
            mark_safe(m - 1, j)  # Bottom border

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                mark_safe(nx, ny)

        # Step 2: Flip all remaining 'O's to 'X', and flip 'S' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

        return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#board =[["X","O","X"],["X","O","X"],["X","O","X"]]
Solution().solve(board)
