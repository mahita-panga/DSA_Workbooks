"""
2251. Number of Flowers in Full Bloom

"""
import bisect
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        #Sweepline Algorithm
        #Event determination
        #Event Sort
        #Active Set
        #Event Processing
        #Binary search on event ranges for queries

        events = []
        for start,end in flowers:
            events.append((start,'start'))
            events.append((end+1,'end'))

        events.sort(key=lambda x:(x[0],x[1]=='start')) #Sort events; prioritize 'start' before 'end' if on the same day i.e. flower event (3,3) => (3,start),(3,end)

        cnt = 0
        flowers_in_bloom = {}

        for pos,event_type in events:
            if event_type == 'start':
                cnt += 1
            elif event_type == 'end':
                cnt -= 1
            flowers_in_bloom[pos] = cnt


        # print(flowers_in_bloom) #This contains event day specific actions

        # Convert bloom_counts to a sorted list of days and counts
        days = sorted(flowers_in_bloom.keys())
        counts = [flowers_in_bloom[day] for day in days]
        result = []
        for arrival in people:
            # Find the nearest day <= arrival
            idx = bisect.bisect_right(days, arrival)-1  #In case the event lies before the found element then we have to do -1.
            if idx >= 0:
                result.append(counts[idx])
            else:
                result.append(0)  # No flowers in bloom before the first bloom day

        return result
