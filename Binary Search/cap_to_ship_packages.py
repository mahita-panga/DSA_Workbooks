"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
Why not dp:
    -- We can technically formulate a DP (e.g., dp[i][d] = min max-weight to ship first i packages in d days), but:
	•	State space would be O(N×D) = 500×500 = 250,000 (still fine).
	•	But transition involves scanning backwards through all previous positions → making it O(N²×D) in worst case.
	•	This becomes TLE and unnecessary for this problem.
Greedy - NOT an option because we dont know what capacity to start with


Think of it as Binary search problem rather than trying greedy or dp approaches
Key hint: The container should definitely pick all the packages and should not discard anything
so, we start at max(arr) as our lower bound

For upper bound, we can do sum(arr) -> means all packages shipped in 1 day

Now try to search for the real value of capacity and calculate the amnt of days it takes to ship for each capacity. If it is == days, then return else continue searching
"""
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def canShip(capacity):
            days_needed = 1
            curr_load = 0
            for weight in weights:
                if curr_load + weight > capacity:
                    days_needed += 1
                    curr_load = 0
                curr_load += weight
            return days_needed <= D

        lb, ub = max(weights), sum(weights)

        while lb < ub:
            mid = (lb + ub) // 2
            if canShip(mid):
                ub = mid
            else:
                lb = mid + 1

        return lb
