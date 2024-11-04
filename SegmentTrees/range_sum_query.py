"""
307. Range Sum Query - Mutable

"""
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = [0]*len(nums)+nums
        for i in range(len(nums)-1,0,-1):
            self.segTree[i] = self.segTree[i<<1] + self.segTree[i<<1|1]
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        pos = index+self.n
        self.segTree[pos] = val
        while pos>1:
            pos = pos>>1 #Find the parent
            self.segTree[pos] = self.segTree[pos<<1]+self.segTree[pos<<1|1] #Update the parent


    def sumRange(self, qs: int, qe: int) -> int:
        left = qs+self.n
        right = qe+self.n+1
        ans = 0
        while left<right:
            if left&1: #left is a odd index => the entire tree can be considered
                ans = ans+self.segTree[left]
                left+=1
            if right&1: #right is odd index => entire tree in right-1 index can be considered
                right-=1
                ans = ans+self.segTree[right]
            left >>=1 #update left to move to parent
            right >>=1 #update right to move to parent
        return ans




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
