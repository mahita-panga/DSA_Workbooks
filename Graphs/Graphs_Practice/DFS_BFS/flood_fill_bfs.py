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

    I have done BFS since it was easy to write.
    -> q.add(sr,sc) <- since we will start our coloring from this node.
    -> until q is empty:
        -> check all 4 directions:
            -> fill color if any node has original color.
            -> add colored node to q.
"""

from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        q = deque()
        image[sr][sc] = color
        q.append((sr, sc))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == original_color:
                    q.append((nx, ny))
                    image[nx][ny] = color

        return image

# Test the function
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
result = Solution().floodFill(image, sr, sc, color)
print(result)
