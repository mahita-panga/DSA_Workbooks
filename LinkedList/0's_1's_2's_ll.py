'''
	Your task is to segregate the list of
	0s,1s and 2s.

	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	---

    ### Intuition:
    - **Bruteforce approach**: Traverse the linked list and store 0's, 1's, and 2's separately in three different lists or arrays. After traversal, reconstruct the linked list by first appending 0's, then 1's, and finally 2's.
    - **Space Complexity**: O(N) due to additional storage.

    - **Optimized approach**: Use three separate pointers (`zeroptr`, `oneptr`, `twoptr`) to directly build lists for 0's, 1's, and 2's during a single traversal. This eliminates the need for extra space, except for pointers.

    ---

    ### Steps:
    1. **Initialize pointers**:
        - `zeroHead, zeroptr` for 0's
        - `oneHead, oneptr` for 1's
        - `twoHead, twoptr` for 2's

    2. **Traverse the linked list**:
        - For each node, depending on its value (0, 1, or 2), append it to the corresponding list (`zeroptr`, `oneptr`, or `twoptr`).

    3. **Terminate and link lists**:
        - Make sure the 0's list (`zeroptr`) is linked to the start of the 1's list (`oneHead`) and the 1's list is linked to the 2's list (`twoHead`).
        - Ensure the last node of the 2's list points to `None`.

    4. **Return the new head**:
        - Return the head of the combined list starting from `zeroHead`.

    ---

    ### Final pointer updates:
    - `zeroptr.next = oneHead.next` (link 0's to 1's)
    - `oneptr.next = twoHead.next` (link 1's to 2's)
    - `twoptr.next = None` (terminate list)

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        zeroHead = zeroptr = Node(-1)
        oneHead = oneptr = Node(-1)
        twoHead = twoptr = Node(-1)
        curr = head
        while curr !=None:
            if curr.data==0:
                zeroptr.next = curr
                zeroptr = zeroptr.next
            elif curr.data==1:
                oneptr.next = curr
                oneptr = oneptr.next
            elif curr.data==2:
                twoptr.next = curr
                twoptr = twoptr.next

            curr = curr.next

        # Terminate each of the lists properly
        # In case of short lists like 0 2 , without termination it fails
        zeroptr.next = None
        oneptr.next = None
        twoptr.next = None

        zeroptr.next = oneHead.next
        if zeroptr.next is None:  # If no ones exist, link to twos
            zeroptr.next = twoHead.next
        else:
            oneptr.next = twoHead.next  # Connect one list to two list


        return zeroHead.next
