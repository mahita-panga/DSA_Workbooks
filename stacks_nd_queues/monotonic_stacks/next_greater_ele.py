"""
https://leetcode.com/problems/next-greater-element-i/

-- Monotonic stack which implies it is either strictly increasing or strictly decreasing
-- here for nge, we traverse from right of array to left.
ex - 4, 12, 3, 5 ,6, 2
st = []

r->l:
    2 - st.emppty(), nge - -1
    st = [2]

    6, 6>top, top cannot be nge, so pop until found or empty as this popped ele can not be nge for any prior ele, 6 will be nge for all those
      st - [] , nge -1
      st - [6]
    5, 5<6 - nge = 6
      st- [6,5]
    3, 3<5 - nge=5
      st [6,5,3]
    12 12<3 x- pop(), 12<5 x -pop() and so on
     st =[], nge -1
      st= [12]
    4 4<12 nge= 12
      st = [12,4]

ans = [12,-1,5,6,-1,-1]

"""
from DP.DP_Practice.2D_DP import 2d_ninja_training
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m_stack = []
        nge = {} #ans
        #traverse from right end of array to find the nge of each value.
        # check if curr val is < top then pop the stack until we find a greater ele. if stack is empty then
        for num in reversed(nums2):
            # if num < top, top is nge, push num else keep popping until we see nge or st is empty
            while m_stack and num >= m_stack[-1]:
                m_stack.pop()

            nge[num] = m_stack[-1] if m_stack else -1
            m_stack.append(num)

        return [nge[x] for x in nums1]
