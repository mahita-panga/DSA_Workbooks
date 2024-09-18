"""
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

-> tempHead at head
-> Travel k nodes, if k-nodes found then:
    -> keep tempHead at kthNode.next
    -> kthNode.next = Null
    -> Reverse tempHead till kthNode and get currHead,currTail
    -> Assign this reversed kth nodes to currTail
->Else:
    return head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
class Solution:
    def reverse_ll(self, head: ListNode) -> None:
        tail = head
        cur, prev = head, None

        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next

        return prev,tail


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or head is None or head.next is None:
            return head

        cur = head
        for _ in range(k-1): #since it is 0th index.
            if cur:
                cur = cur.next

        # in case cur=None, means the LL is of size < k
        if cur: # remaining LL >= k size
            temp_next = cur.next
            cur.next = None # break link for reversing
            cur_head, cur_tail = self.reverse_ll(head)
            cur_tail.next = self.reverseKGroup(temp_next, k) # next reversing
            return cur_head

        else: # remaining LL is < k size -> dont touch anything
            return head
