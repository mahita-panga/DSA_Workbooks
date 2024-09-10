"""
19. Remove Nth Node From End of List

Bruteforce approach:
   -> Traverse the list to find its length,
    and then traverse again to reach the node that is length - n from the start. Remove that node. This approach requires two passes through the linked list.
	•	Space Complexity: O(1), but requires two passes.
Optimized Way:
    fast and slow pointer approach:
        Use two pointers, fast and slow,
        where fast moves n steps ahead of slow.
        When fast reaches the end, slow will be at the node before the one to remove.
	-> This ensures a single traversal.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #fast ptr moves n steps
        i = n
        fast = slow = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next!=None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
