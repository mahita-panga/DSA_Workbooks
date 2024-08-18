"""
https://leetcode.com/discuss/interview-question/5633414/Google-Repeating-questions

An stone array is given.
A mouse is on index 0 initially, he starts jumping towards right.
Score of a jump is = (len of jump * value of stone mouse is jumping on to)
for eg : Score of jump from i to j, score would be = (j-i)*stone[j]
Mouse can make any number of jumps, find what is the maximum score that can be achieved.

ex
3 5 4 7 2 12 8 10 1

ex: 3 to 12 (512) + 12 to 10 (210) + 10 to 1 (1*1) = 81

INTUITION:
    We need to maximize the score this mouse can get
    Initialization: Take a dp array which stores the max score at the index.
    Objective: This dp[n-1] stores the max possible value it takes to reach n-1
    Action: dp[j] = max(dp[j],dp[i]+(j-i)*stones[j])


"""

class Solution:
    def maxScore(self,stones):
        n = len(stones)
        dp = [0]*n

        for i in range(n):
            for j in range(i+1,n):
                dp[j] = max(dp[j],dp[i]+(j-i)*stones[j])
        return dp[n-1]
stones = [3, 5, 4, 7, 2, 12, 8, 10, 1]
print(Solution().maxScore(stones))

# ABOVE IS O(N^2) TC and O(N) SC
# CAN be further optimized
# We only need max score till the previous stone to make a decision.
#
class Solution2:
    def maxScore(self,stones):
        n = len(stones)
        dp = [0]*n
        max_so_far = 0

        for i in range(n):
            dp[i] = max_so_far+stones[i]
            max_so_far = max(max_so_far,(dp[i]-i)*stones[i])
        print(dp)
        return dp[n-1]

stones = [3, 5, 4, 7, 2, 12, 8, 10, 1]
print(Solution2().maxScore(stones))
