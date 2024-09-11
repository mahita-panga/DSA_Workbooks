"""
141. Linked List Cycle
To detect cycle, we use:
    ->two pointers:
        -> Fast moves 2 steps each time
        -> slow moves 1 step each time
    -> This will make sure that at any point if there is a cycle then fast and slow will intersect.
    -> If intersected, then return True else False

"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None or head.next.next==None:
            return False
        fast = head.next.next
        slow = head
        while fast!=None and fast.next!=None:
            if slow==fast:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
