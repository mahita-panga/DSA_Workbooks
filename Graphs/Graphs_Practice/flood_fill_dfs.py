"""
LC #733: FLOOD FILL
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.

Intuition:
    Since the image is a matrix, we can use a traversal technique, either BFS or DFS.
    -> Identify the color in image[sr][sc]
    -> if original_color == new_color, then dont modify the image
    -> otherwise do bfs/dfs traversal and fill all matrices in 4 directions which has original color to new color.
    -> DFS: Depthwise traverse the vertices in all 4 directions.
    -> Base case for this recursion: in case the indices are overflowing then return
    or incase the color is not same as original then return
"""

from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x,y):
            #BASE CONDITIONS for recursion:
            # In case x or y overflow beyond the co-ordinates, return or if color is not original, then return
            if x<0 or x == len(image) or y<0 or y==len(image[0]):
               return
            if image[x][y] != original_color:
                return

            image[x][y] = color

            for dx,dy in directions:
                dfs(x+dx,y+dy)

        dfs(sr,sc)

        return image

# Test the function
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
result = Solution().floodFill(image, sr, sc, color)
print(result)
