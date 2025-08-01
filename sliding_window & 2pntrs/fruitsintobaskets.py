"""
904. Fruit Into Baskets
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Intn:
    •   Use a sliding window to track at most 2 types of fruits.
	•	Expand the window (r) by adding fruits.
	•	If we exceed 2 types, shrink the window from the left (l) until valid.
	•	Update the max length of valid window during each step.
"""
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l = 0
        cntr = Counter()
        max_len = 0

        for r in range(len(fruits)):
            cntr[fruits[r]] += 1

            while len(cntr) > 2:
                cntr[fruits[l]] -= 1
                if cntr[fruits[l]] == 0:
                    del cntr[fruits[l]]
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
