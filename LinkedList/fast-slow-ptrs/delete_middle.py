"""
2095. Delete the Middle Node of a Linked List
-> Reach Middle
-> Delete Middle
"""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None

        fast = head.next.next if head.next else None
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if slow.next:
            node = slow.next.next
            slow.next = node
        return head
