"""
GFG: https://www.geeksforgeeks.org/problems/geeks-training/1

Intuition:
    Recursion:
        Information we need to pass: day and the index of the activity picked
        f(day,index): Denotes the total points that ninja can have for performing
        activity at index on day.
        Action we need to perform: Pick up all activities except the activity as index.
        Base condition:
            If day==0: return maximum points among all the activities on day 0

"""
from typing import List
#MEMOIZATION
class Solution:
    def max_points(self,day,last_activity,dp,ninja_mat):
        if dp[day][last_activity] != -1:
            return dp[day][last_activity]
        if day == 0: #Base case
            max_i = 0
            for i in range(3):
                if i!= last_activity:
                    max_i = max(max_i,ninja_mat[0][i])
            dp[day][last_activity] = max_i
            return dp[day][last_activity]

        max_i = 0
        for i in range(3):
            if i!= last_activity:
                activity = ninja_mat[day][i] + self.max_points(day-1,i,dp,ninja_mat)
                max_i = max(max_i,activity)
        dp[day][last_activity] = max_i
        return dp[day][last_activity]


    def ninja_activity(self,ninja_mat: List(List)) -> int:
        day = len(ninja_mat)-1
        dp = [[-1 for _ in range(4)] for _ in range(day)]
        return self.max_points(day,3,dp,ninja_mat)

#TABULATION
class Solution:
    def maximumPoints(self,ninja_mat,n) -> int:
        #FIRST RULE OF TABULATION: Declare same size array as the input.
        dp = [[-1 for _ in range(4)] for _ in range(n)]
        #SECOND RULE: INTIALIZE ARRAY WITH BASE CASE
        #BASE CASE IS DAY 0
        #dp[i][j] -> no.of points achieved on ith day given that j activity is performed before day
        dp[0][0] = max(ninja_mat[0][1],ninja_mat[0][2]) #if last_activity is 0, then on day0 choice would be max(act1,act2)
        dp[0][1] = max(ninja_mat[0][0],ninja_mat[0][2])
        dp[0][2] = max(ninja_mat[0][0],ninja_mat[0][1])
        dp[0][3] = max(ninja_mat[0][0],ninja_mat[0][2],ninja_mat[0][1])
        #activity 3 indicates when no activity has been performed yet <- this is considered only during starting
        for day in range(1,n):
            for last_activity in range(4):
                maxi = 0
                for task in range(3):
                    if task!=last_activity:
                            # Calculate the total points for the current day's activity and
                            # the previous day's maximum points.
                        maxi= max(maxi,ninja_mat[day][task]+dp[day-1][task])
                dp[day][last_activity] = maxi
        return dp[n-1][3]
