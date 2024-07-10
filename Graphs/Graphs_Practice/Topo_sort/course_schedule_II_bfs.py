"""
LC #210: https://leetcode.com/problems/course-schedule-ii/description/

Using BFS:
    -> Create adj list out of the courses
    -> Indegree represent num of incoming degrees for a vertex
    -> add all nodes with indegree 0 to the queue
    -> Until queue is empty:
        -> pop the queue
        -> add the ele to result
        -> for all its neighbours,
        -> reduce indegree by 1 indicating we have traversed
        -> if it is 0, add to queue

    -> if len(result) != n i.e it is not a cyclic graph:
        return result

"""
from typing import List
from collections import deque

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        sorted_order = []
        # if n is smaller than or equal to zero we will return the empty array
        if n <= 0:
            return sorted_order

        # Store the count of incoming prerequisites in a hashmap
        in_degree = {i: 0 for i in range(n)}
        # a. Initialize the graph
        graph = {i: [] for i in range(n)}  # adjacency list graph

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[1], prerequisite[0]
            graph[parent].append(child)  # add the child to its parent's list
            in_degree[child] += 1  # increment child's in_degree

        # c. Find all sources i.e., all nodes with 0 in-degrees
        sources = deque()
        # traverse in in_degree using key
        for key in in_degree:
            # if in_degree[key] is 0 append the key in the deque sources
            if in_degree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sorted_order and subtract one from
        # all of its children's in-degrees. If a child's in-degree becomes zero,
        # add it to the sources queue
        while sources:
            # pop an element from the start of the sources and store
            # the element in vertex
            vertex = sources.popleft()
            # append the vertex at the end of the sorted_order
            sorted_order.append(vertex)
            # traverse in graph[vertex] using child
            # get the node's children to decrement
            # their in-degrees
            for child in graph[vertex]:
                in_degree[child] -= 1
                # if in_degree[child] is 0 append the child in the deque sources
                if in_degree[child] == 0:
                    sources.append(child)

        # topological sort is not possible as the graph has a cycle
        if len(sorted_order) != n:
            return []

        return sorted_order
