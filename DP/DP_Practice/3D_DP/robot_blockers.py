"""
Given two inputs,
First input is
the location map,
a 2D array in which each cell contains 0/ E/ X
0 = Robot, E = Empty, X = blocker
Second input is the query. It's a 1D array consisting of distance to the closest blocker in the order fro bottom and right
[2,2,4,1]
→ This means distance of 2 to the left blocker, 2 to the top blocker, 4 to the bottom block
the right blocker
Write a function that takes these two inputs and returns the index of the robots (if any) that matches th
we're looking for.
Input:

OEEEX
EOXXX
EEEEE
XEOEE
XEXEX
[2, 2, 4, 1]

"""
def find_robots(grid, query):
    M = len(grid)
    N = len(grid[0])

    # dp[i][j][0] -> top, dp[i][j][1] -> left, dp[i][j][2] -> bottom, dp[i][j][3] -> right
    dp = [[[1] * 4 for _ in range(N)] for _ in range(M)]

    # First pass helps identify top and left blockers
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "X":  # A blocker means 0 distance to itself
                dp[i][j][0] = dp[i][j][1] = 0
            else:
                if i > 0:  # Distance from top
                    dp[i][j][0] = dp[i-1][j][0] + 1
                if j > 0:  # Distance from left
                    dp[i][j][1] = dp[i][j-1][1] + 1

    # Second pass to fill right and bottom blockers
    for i in range(M-1, -1, -1):
        for j in range(N-1, -1, -1):
            if grid[i][j] == "X":  # A blocker means 0 distance to itself
                dp[i][j][2] = dp[i][j][3] = 0
            else:
                if i < M-1:  # Distance from bottom
                    dp[i][j][2] = dp[i+1][j][2] + 1
                if j < N-1:  # Distance from right
                    dp[i][j][3] = dp[i][j+1][3] + 1

    # Extract the query distances
    left, top, bottom, right = query  # Left, top, bottom, right

    result = []

    # Compare the robots' distances to the query distances
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "O":  # Only check robot cells
                if (dp[i][j][1] == left and  # Left distance
                    dp[i][j][0] == top and   # Top distance
                    dp[i][j][2] == bottom and  # Bottom distance
                    dp[i][j][3] == right):  # Right distance
                    result.append([i, j])

    return result


# Example input
grid = [
    ['O', 'E', 'E', 'E', 'X'],
    ['E', 'O', 'X', 'X', 'X'],
    ['E', 'E', 'E', 'E', 'E'],
    ['X', 'E', 'O', 'E', 'E'],
    ['X', 'E', 'X', 'E', 'X']
]

query = [2, 2, 4, 1]

# Output the result
print(find_robots(grid, query))  # Expected output: [[1, 1]]
