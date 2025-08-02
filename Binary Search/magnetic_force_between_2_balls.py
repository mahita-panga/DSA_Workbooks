"""
https://leetcode.com/problems/magnetic-force-between-two-balls/


"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """ BINARY SEARCH + GREEDY
        NOT DP - dp[ith ball][jth pos] constraints and backtracking - infeasible

        if we can place balls such that min force is x, then we can do this for all <x ...if we cannot place ball at x, then we can do it somewhere which has >x

         magnetic force ans search space = min(array), max(arr)
         in this space, choose the force such that place balls in that distance is possible.

         1,2,3,4,7 - (1,7) - force or gap- 4, check if you can place the balls

        """

        def can_place_balls(x):
            """ Greedily place the balls in positions, if possible place it and if not move to the next available pos and place it there. """
            prev_ball_pos = position[0]
            balls_placed = 1
            for i in range(1, len(position)):
                curr_pos = position[i]
                if curr_pos - prev_ball_pos >= x:
                    balls_placed += 1
                    prev_ball_pos = curr_pos
                    if balls_placed == m:
                        return True
            return False

        position.sort()
        ans = 0
        l,r = 1,  position[-1] - position[0]
        while l<=r:
            mid = (l+r)//2
            if can_place_balls(mid):
                ans = mid
                l = mid+1
            else:
                r = mid -1

        return ans
