"""
DOUBLY LINKED LIST

    <- | |val| | ->
prev     curr      next

"""

#DELETING FROM DLL

class Solution:
    #INSERTING INTO DLL
    def insertDLL(self,head,value):

    #REVERSING A DLL
    def reverseDLL(self, head):
        # Return head of reverse doubly linked list
        curr = head
        last = None #Keeps track of prev link.
        while curr is not None: #Until curr reaches last
            last = curr #last is set at curr position
            curr.prev, curr.next = curr.next, curr.prev  # Swap next and prev pointers of curr
            curr = curr.prev  # Move to next node, which is the original prev node
        # After the loop, last will point to the old head,
        # but since the list is reversed, the new head is last.
        if last:
            return last  # The last node becomes the new head
        return head #Case in case dll has only 1 node.
