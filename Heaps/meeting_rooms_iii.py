"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.
You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.
"""

##https://leetcode.com/problems/meeting-rooms-iii/solutions/4509113/python3-one-heap-and-two-heaps-solutions-all-meeting-rooms-solutions

##

import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0]) # process meetings by start time
        avail_rooms = [i for i in range(n)] # heap of room_ids
        heapq.heapify(avail_rooms)
        rooms = [] # heap of (end_time, room_id)
        result = [0 for _ in range(n)]
        for start, end in meetings:
            # release previous meetings
            while rooms and rooms[0][0] <= start:
                _, room_id = heapq.heappop(rooms)
                heapq.heappush(avail_rooms, room_id)

            # scenario 1: rooms available: find the lowest room_id
            if avail_rooms:
                min_room_id = heapq.heappop(avail_rooms)
                result[min_room_id] += 1
                heapq.heappush(rooms, (end, min_room_id))
            # scenario 2: all rooms occupied, schedule to first available room first (smallest room_id if same end time)
            else:
                prev_end, room_id = heapq.heappop(rooms)
                result[room_id] += 1
                heapq.heappush(rooms, (prev_end + end - start, room_id))

        min_meetings, ans = -1, None
        for room_id in range(n):
            if result[room_id] > min_meetings:
                ans = room_id
                min_meetings = result[room_id]
        return ans
