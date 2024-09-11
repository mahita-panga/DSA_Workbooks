"""
LINKED LIST
-> Declaration
-> Insertion
-> Deletion
-> Reversal
"""

class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class Solution():
    def insert_at_index(self, head, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.next = head
            return new_node
        current = head
        for _ in range(index - 1):
            if current is None:
                return head
            current = current.next
        if current is None:
            return head
        new_node.next = current.next
        current.next = new_node
        return head

    def delete_from_start(self, head):
        if head is None:
            return None
        return head.next

    def delete_from_end(self, head):
        if head is None or head.next is None:
            return None
        current = head
        while current.next.next: #UNTIL LAST NODE IS EMPTY
            current = current.next
        current.next = None
        return head

    def reverse_list(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

"""
LC 237. Delete Node in a Linked List

To delete the given node, we copy the value of the next node to the current node and adjust the next pointer to skip the next node.
Copy the value of the next node to the current node.
Adjust the next pointer to skip the next node.
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

"""
Find middle of LL
Tortoise Hare Method / slow-fast pntrs
-> slow moves 1 step
-> fast moves 2 steps
=> By the time fast reaches end, slow will be in the middle.

"""
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast,slow = head ,head
    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
    return slow
