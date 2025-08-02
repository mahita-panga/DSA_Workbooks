"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

	•	Why ceil for all but last? Due to train departure constraints — each train can only leave on the hour (except last).
	•	Upper bound? 10^7 is safe as per problem constraints.
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # constraints - too big for dp
        # search space on speed to identify which speed is ideal to reach offc
        # space bounds - (1, max_possible_speed)  <- max_speed can be highest bound to check because we dont have any limit on speed of train based on the given distance or time req.
        # tot = sum([(dist[i])//m for i in range(n)]) --- calc is wrong as it does not account for the condition where all trips should start at int hr except the last

        n = len(dist)
        l,h = 1, 10**7 + 1
        ans = -1

        while l<h:
            m = (l+h)//2
            tot = sum([math.ceil(dist[i]/m) for i in range(n-1)])
            tot += dist[-1]/m
            if tot > hour:
                l = m + 1
            else:
                ans = m
                h = m
        return ans
