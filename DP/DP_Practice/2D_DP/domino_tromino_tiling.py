"""
790. Domino and Tromino Tiling

https://leetcode.com/problems/domino-and-tromino-tiling/solutions/1620975/c-python-simple-solution-w-images-explanation-optimization-from-brute-force-to-dp(REFER POSSIBLE DIAGRAMS ONLY)
"""
class Solution:
    def numTilings(self, n: int) -> int:

        @lru_cache(None)  # Use lru_cache for memoization to improve performance
        def count_ways(first_row: int, second_row: int) -> int:
            # Base case: If we exceed the board size, there's no way to tile.
            if first_row > n or second_row > n:
                return 0
            # Base case: If both rows are completely tiled, we've found one valid tiling.
            if first_row == n and second_row == n:
                return 1

            # Initialization of possible ways to tile.
            ways = 0
            # When both rows have the same number of points covered by tiles.
            if first_row == second_row:
                ways = (
                    count_ways(first_row + 2, second_row + 2) +  # Place a 2x2 square.
                    count_ways(first_row + 1, second_row + 1) +  # Place two 2x1 tiles, one in each row.
                    count_ways(first_row + 2, second_row + 1) +  # Place a 'L' shaped tromino.
                    count_ways(first_row + 1, second_row + 2)    # Place an inverted 'L' shaped tromino.
                )
            elif first_row > second_row:
                # If the first row has more tiles than the second row.
                ways = count_ways(first_row, second_row + 2) + count_ways(first_row + 1, second_row + 2)
            else:
                # If the second row has more tiles than the first row.
                ways = count_ways(first_row + 2, second_row) + count_ways(first_row + 2, second_row + 1)

            # Return the ways modulo MOD, which represents the maximum number of unique tilings.
            return ways % MOD

        # Define the modulo constant to prevent large number arithmetic issues.
        MOD = 10**9 + 7
        # Call the helper function with the initial states of the board (0 tiles placed).
        return count_ways(0, 0)
