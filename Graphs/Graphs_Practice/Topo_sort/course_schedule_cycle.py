"""
LC #207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

i.e. "We have [course_to_take, prereq.]"

Intuition :
    -> Since, we are given courses that we need to take before a certain course,
    we can create a graph i.e. adjacency list out of this information.
    -> Along with adjacency list, we also need to consider indegree of these source
    vertices(courses) i.e. no.of courses to take. This is to ensure, we are traversing
    all courses that dont have any prerequisites too.
    * in_degree[i] is the number of prerequisites for course i.

    -> Add all courses with indegree-0 to the queue.
    -> Have taken_courses = 0
    -> Perform bfs traveral and process each course in queue:
        -> taken_courses+=1 i.e. we have taken this course
        -> For each dependent course (neighbor),
              ->it decrements its in-degree.
              -> If the dependent course's in-degree becomes 0,
              it means all its prerequisites have been satisfied, so it's added to the queue.
    -> if taken_courses == num_courses then we are able to cover all courses else we are not and a
    cycle is present

"""
from typing import List
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We need to check if there is a cycle in this graph i.e. while traversing, if we are visiting same node twice then return false else true.
        if numCourses <= 0:
            return False

        # Step 1: Build the adjacency list and in-degree array
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1

        # Step 2: Initialize the queue with courses that have no prerequisites
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        courses_taken = 0

        # Step 3: Process each course in the queue
        while queue:
            course = queue.popleft()
            courses_taken += 1

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses can be taken
        return courses_taken == numCourses


numCourses = 3
prerequisites = [[1,0],[0,1]]
Solution().canFinish(numCourses,prerequisites)
