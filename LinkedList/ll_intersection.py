"""
160. Intersection of Two Linked Lists
Optimal:
    -> Using fast/slow pointer approach
    -> fast will be n steps ahead of slow where n is the difference between lengths of ll
    -> Now both fast and slow will start moving together.
    -> The point where they collide is the answer

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        l1 = 0
        while curr1!=None:
            l1+=1
            curr1 = curr1.next

        l2 = 0
        while curr2!=None:
            l2+=1
            curr2 = curr2.next

        diff = 0
        fast,slow = None,None
        if l1>l2:
            diff = l1-l2
            fast = headA
            slow = headB
        else:
            diff = l2-l1
            fast=headB
            slow=headA

        while diff>0:
            fast = fast.next
            diff-=1
        while fast!=None and slow!=None:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None
