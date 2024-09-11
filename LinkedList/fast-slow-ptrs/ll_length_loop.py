"""
Find length of the loop

->First, detect the cycle using the slow-fast pointer (tortoise-hare) approach.
-> If a cycle is found, start counting nodes by traversing the cycle from the meeting point, returning to the same point.
-> To count the nodes in the cycle, keep moving a pointer around the loop until it meets the starting point again.

This approach has O(N) time complexity and O(1) space complexity.
"""

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        if head==None or head.next==None:
            return 0
        fast = head
        slow = head
        while fast!=None and fast.next!=None:

            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                #Detect point where cycle is
                cnt = 1
                temp = slow
                while temp.next != slow:
                    cnt+=1
                    temp = temp.next
                return cnt
        else:
            return 0
