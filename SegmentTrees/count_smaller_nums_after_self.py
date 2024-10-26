"""
315. Count of Smaller Numbers After Self


"""

#Intuition for segment tree here: Identifying the smaller elements to right i.e. range query for all numbers smaller than self in [i+1,n] if i is self index
#What to save in the segment tree i.e. range query: Since we have to get the counts of elements,we can store the counts of min value in the array <- aggregate func
#What will be the leaf nodes: Since the values of the array can range between negative to positive, better to do coordinate compression technique and map the values to the array indices
#For each ele, query the segment tree to get the count of the elements.
from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        #create a rank_map which can be used for cordinate compression
        rank_map = {val:idx for idx,val in enumerate(sorted_nums)}
        n = len(sorted_nums)
        #SEGMENT TREE
        segtree =  [0]*2*n

        def update_index(index,val):
            nindex = index+n
            segtree[nindex] += val
            while nindex>1:
                nindex >>=1
                segtree[nindex] = segtree[nindex<<1]+segtree[nindex<<1|1]
            # print(segtree)

        def query(qs,qe,n):
            res = 0
            left = qs+n
            right = qe+n+1
            while left<right:
                if left&1:
                    res += segtree[left]
                    left+=1
                if right&1:
                    right-=1
                    res += segtree[right]
                left >>= 1
                right >>=1
            return res

        #PROCESS THE ELEMENTS FROM RIGHT TO LEFT
        counts = []
        for num in reversed(nums):
            r = rank_map[num]
            #query asks the segment tree for the cumulative count of all values smaller than num up to but not including num’s rank r.
            counts.append(query(0,r-1,n)) # Count of elements smaller than the current element <- get the value of the element from segtree
            #After querying, we update the segment tree to include the current element, incrementing the count at index r.
            update_index(r,1) #Update the segment tree to add this element
        counts.reverse()
        return counts

"""
#Example nums = [5, 2, 6, 1].
sorted: [1,2,5,6]
rank_map = {1:0,2:1,5:2,6:3}
for reversed nums
=> for each 1 6 2 5:
    num =1
    r = 0
    query(0,-1): empty, so: 0
    update(r,0) => segtree holds 1 at leaf node (1,0,0,0)
     1
    1 0 0 0

    num=6
    r=3
    query(0,2): returns 1 because of 1
    update(r,3) => segtree holds 1 at 3rd index (1,0,0,1)
    tree:
          2
         1  1
        1 0 0 1

    num=2
    r=1
    query(0,0): returns 1 because of 1
    update(r,1) => segtree is now (1,1,0,1)

    num=5
    r=2
    query(0,1): returns 2 because of 1,2
    update(r,2)=> (1,1,1,1)

    res: [0 1 1 2]
    reverse this for final ans: [0 1 1 2]
"""
