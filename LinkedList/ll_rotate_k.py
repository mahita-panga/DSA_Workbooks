"""
61. Rotate List

-> Find the length
-> Make ll circular
-> No. of rotations req is k%len
-> Move head to len-no of rotation and keep a prev pointer
-> break the connect at prev and set to None.
-> Now head is at the point where the rotation should start.\

Time Complexity: O(N), Space Complexity: O(1).
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        curr = head
        prev = None
        len_ll = 0
        while curr!=None:
            len_ll+=1
            prev = curr
            curr=curr.next
        prev.next = head #Made it circular
        rotations = k%len_ll
        move = len_ll - rotations
        tmp = None
        while move>0:
            tmp = head
            head = head.next
            move-=1
        tmp.next=None
        return head
