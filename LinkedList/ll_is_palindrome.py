"""
234. Palindrome Linked List

-> Reach the middle of the LL
-> Reverse the LL
-> Check the values

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first,sec = head, prev
        while sec!=None:
            if first.val != sec.val:
                return False
            first = first.next
            sec = sec.next
        return True
