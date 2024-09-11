"""
142. Linked List Cycle II
-> Find the cycle node.

    •	Use two pointers, slow and fast (tortoise and hare method).
	•	Move slow by 1 step and fast by 2 steps.
	•	If slow meets fast, a cycle exists; otherwise, there’s no cycle.
	•	Reset slow to head, and move both pointers by 1 step until they meet again. The meeting point is the cycle’s start.

This approach runs in O(N) time and uses O(1) space.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        fast = head
        slow = head
        while fast!=None and fast.next!=None:

            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                #Detect point where cycle is
                break
        else:
            return None

        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow
