"""
328. Odd Even Linked List
Requirement: Sp:O(1)
Intuition:
    Bruteforce way: Traverse LL, save add odd ptrs to list and once odd exhausts, traverse even
    and add it to list. Traverse list and update LL values accordingly
    Requires Sp:O(N)
-> To save on the space complexity we can:
    use a event ptr to traverse even items and odd ptr for odd items
    at end we need to point odd ptr back to even's starting ptr.
    So we save that in evenHead.

    Steps:
        -> oddptr = head
        -> evenptr, evenHead = head.next

    Since even is anyways ahead of odd, we will verify if even reached the end of list
    Update the pointers as:
        odd.next = odd.next.next
        odd = odd.next //Updating the odd ptr to two steps ahead

        even.next = event.next.next
        even = even.next

    odd.next = evenHead

    This way we have updated the ll ptrs accordingly.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        odd = head
        even = head.next
        evenHead = head.next
        while even!=None and even.next!=None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head
