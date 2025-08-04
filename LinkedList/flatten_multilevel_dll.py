"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
"""
Recursion to flatten the list
-> if we see child node, call recursion which will flatten it i.e traverse the list and insert into main list
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        def flatten_dfs(node: 'Node') -> 'Node':
            curr = node
            last = node  # This will track the tail of the flattened list

            while curr:
                next_node = curr.next

                if curr.child:
                    # Flatten the child list
                    child_head = curr.child
                    child_tail = flatten_dfs(child_head)

                    # Connect curr <-> child_head
                    curr.next = child_head
                    child_head.prev = curr

                    # If next_node exists, connect child_tail <-> next_node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    # Clear the child pointer
                    curr.child = None

                    # Update last to child_tail
                    last = child_tail
                    curr = next_node
                else:
                    last = curr
                    curr = next_node

            return last

        flatten_dfs(head)
        return head
"""
other option - use stack simply
stack when traversing the childlist.
when sublist ends, pop and continue the mainlist
"""
class OpSolution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        stack = []
        while temp is not None:
            if temp.child is not None:
                if temp.next:
                    stack.append(temp.next)
                temp.next = temp.child
                temp.child= None
                temp.next.prev = temp
            if temp.next is None and len(stack) != 0:
                temp.next = stack.pop()
                temp.next.prev = temp
            temp = temp.next
        return head
