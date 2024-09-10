"""
2. Add Two Numbers LINKED LIST

num1  = 342, num2 = 465

LL rep: l1 = [2,4,3]
LL rep: l2 = [5,6,4]

Result: sum = 807;
LL = [7,0,8]

Intuition:
    -> Traverse both linked lists simultaneously, adding both node values
    and save it in a carry value if the sum exceeds 9.
    -> Use a dummy node to simplify the process of
    building the result list.
    -> Handle the cases where one list is longer than the other
    and add the carry at each step.
    -> Loop traverses till the both the linked lists are empty or the carry_forward is 0
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        tmp = dummy

        carry_for = 0
        while (curr1!=None or curr2!=None) or carry_for:
            ans = 0
            if curr1:
                ans += curr1.val
                curr1 = curr1.next
            if curr2: #Dont put elif!! We need to check both lists
                ans += curr2.val
                curr2 = curr2.next

            res = (ans+carry_for)%10
            carry_for = (ans+carry_for)//10

            res_Node = ListNode(res)
            tmp.next = res_Node
            tmp = tmp.next


        return dummy.next
