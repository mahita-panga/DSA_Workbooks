"""
1395. Count Number of Teams
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Intuition:
    //TO-WRITE
"""


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        smaller = [0] * n
        larger = [0] * n

        for j in range(n):
            for i in range(j):
                if rating[i] < rating[j]:
                    smaller[j] += 1

        for j in range(n):
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    larger[j] += 1

        count = 0
        # Count valid teams
        for j in range(n):
            count += smaller[j] * larger[j]  # for the pattern rating[i] < rating[j] < rating[k]
            count += (j - smaller[j]) * (n - 1 - j - larger[j])  # for the pattern rating[i] > rating[j] > rating[k]

        return count
