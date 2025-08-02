"""
https://leetcode.com/problems/minimum-time-to-repair-cars/description/
"""
from math import sqrt,floor

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Intuition -- Constraints too big for thinking of DP
        -> Another way to look at is to identify the time where all cars would be repaired. => Search on time space.
        -> for a given time, number of cars a person repairs is :
            as mentioned r.n^2 = T
            => n = sqrt(T/r)
            => since we are searching we ensure that n is <= sqrt(T/r)

        -> Time space ranges from [0, min_rank*n*n] for n cars
        """
        def get_cars_repaired_at_t(t):
            tot_cars = 0
            for r in ranks:
                tot_cars += int((t/r)**0.5)

            return tot_cars

        min_rank = max(ranks) #slowest mechanic
        l,r = 1, min_rank*cars*cars

        while l<r:
            mid = (l+r)//2
            cars_repaired_at_t = sum(int((mid / rank) ** 0.5) for rank in ranks) #get_cars_repaired_at_t(mid)
            if cars_repaired_at_t < cars:
                l = mid+1
            else:
                r = mid

        return l
