"""
heapify the counter of this string, then pop the element from heap.
if prev popped element needs to be pushed, push it back
do until heap is empty

if res len is > original s then return ''
"""
#Original version
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        cntr = Counter(s)
        print(cntr)
        max_heap = [(-x[1],x[0]) for x in cntr.items()]
        heapq.heapify(max_heap)
        res = ''
        while max_heap:
            cnt,val = heapq.heappop(max_heap)

            if len(res)>0 and res[-1]==val:
                if max_heap:
                    n_cnt,n_val = heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (cnt,val))
                    cnt,val = n_cnt,n_val

            if len(res)>0 and res[-1]==val:
                return ""

            res += val
            if -1*cnt >1:
                heapq.heappush(max_heap, (cnt+1,val))
        return res


#Cleaner version -- using prev cnt and val for better tracking and removing redundant checks

class BettSolution:
    def reorganizeString(self, s: str) -> str:
        cntr = Counter(s)
        max_heap = [(-x[1],x[0]) for x in cntr.items()]
        heapq.heapify(max_heap)
        res = ''
        prev_cnt,prev_val = 0,''
        while max_heap:
            cnt,val = heapq.heappop(max_heap)
            res += val
            if prev_cnt < 0:
                heapq.heappush(max_heap, (prev_cnt, prev_val))
            prev_cnt, prev_val = cnt+1, val


        return res if len(res)==len(s) else ''
