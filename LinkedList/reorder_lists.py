# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
High level Thought

> find mid in ll
-> reverse mid - end of the ll
->insert ele from mid - end in between first - mid in the ll.

finding mid - fast and slow ptr approach
reversing mid-end - reverse the list - break the list ptr from mid and generate the reverse. prev refers to the reverse list's head

use head and prev nodes to insert or merge the ll.

"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid,end = head, head
        while end and end.next:
            end = end.next.next
            mid = mid.next

        prev = None
        curr = mid.next
        mid.next = None # break the list into two halves

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first, second = head, prev  # 'prev' is the head of reversed list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
