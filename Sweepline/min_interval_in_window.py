"""
1851. Minimum Interval to Include Each Query
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.
You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

"""
from sortedcontainers import SortedList
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #Sweepline Algorithm
            #Event determination
            #Event Sort
            #Prepare Queries
            #Active Set
            #Event Processing
            #Binary search on event ranges for queries
        events = []
        for start,end in intervals:
            events.append((start,'start',end))
            events.append((end,'end',start))

        events.sort(key = lambda x:(x[0],x[1]=='start'))#prefer end intervals to be sorted before event start

        # Step 3: Prepare sorted queries with their indices to store results
        sorted_q = sorted((q, i) for i, q in enumerate(queries))
        res = [-1] * len(queries)  # Placeholder for results in query order

        #INSTEAD OF HEAP, CAN ALSO USE SORTED LIST <- https://leetcode.com/problems/minimum-interval-to-include-each-query/solutions/5421978/sorted-list-sweep-line-algo

        #Step 4: Active intervals (min-heap for minimum length interval at top)
        active_heap = []
        evnt_idx = 0

        # Step 5: Process queries by sweeping through events
        for q, i in sorted_q:
            # Process all events up to the current query point
            while evnt_idx < len(events) and events[evnt_idx][0] <= q:
                pos, e_type, boundary = events[evnt_idx]
                if e_type == 'start':
                    # Push interval length and end point to the heap
                    heapq.heappush(active_heap, (boundary - pos + 1, boundary))
                else:
                    # Remove intervals from the heap that are no longer active beyond the query point
                    while active_heap and active_heap[0][1] < q:
                        heapq.heappop(active_heap)
                evnt_idx += 1

            #THIS IS NEEDED <- without the cleanup, the heap still has the some intervals which are no longer needed for the query point.
            # Clean up the heap to remove any intervals not covering the query point
            while active_heap and active_heap[0][1] < q:
                heapq.heappop(active_heap)

            # Step 6: Assign result for the current query
            if active_heap:
                res[i] = active_heap[0][0]  # The minimum length in the active set

        return res
