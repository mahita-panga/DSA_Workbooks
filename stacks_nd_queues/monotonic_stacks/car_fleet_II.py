"""

https://leetcode.com/problems/car-fleet-ii/description/

-> Stacks can be used // similar to asteroid collision
--
traverse right - left
maintain stack for potential cars which can cause crash
if the cari speed > stack top => definite car crash.
calculate the collision time,
add it to res,
push the new fleet along with ind and time into stack if ind < len(cars). if collision is beyond the purview, we dont need to consider that


"""
from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        st = []
        n = len(cars)
        res = [-1.0]*n

        for i in range(n - 1, -1, -1):
            pos,speed = cars[i]
            while st:
                next_pos, next_speed, next_time = st[-1]
                # current car is slower or same speed - no collision, other cars can be removed
                if speed <= next_speed:
                    st.pop()
                    continue

                coll_time = (next_pos - pos) / (speed - next_speed)

                # If the collision time is greater than when the lead car crashes, it’s invalid
                if next_time == -1 or coll_time <= next_time:
                    break
                else:
                    st.pop()

            if st:
                res[i] = (st[-1][0] - pos) / (speed - st[-1][1])
            st.append((pos, speed, res[i]))

        return res
