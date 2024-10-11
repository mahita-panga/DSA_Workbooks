"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

TC:
Heap Operations: Each insertion and extraction from the heap takes O(nlogn). We perform these operations for each node in the lists, so the total time complexity is O(nlogn), where n is the total number of nodes across all lists.
Overall Time Complexity: O(nlogn).

SC: O(n) + O(n)//heap + ll

SC and TC can be optimized by only saving k nodes at a time in the heap, Only create a min heap out
of k lists with head nodes.
New TC:
Each insertion and extraction from the heap takes O(log k), where k is the number of linked lists. We perform these operations for each node in the lists, so the total time complexity is O(n \log k), where n is the total number of nodes across all lists.
	Overall Time Complexity: O(nlog k).
New SC: O(n+k) k-heap size
"""

# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for l_list in lists:
            while l_list:
                heapq.heappush(minheap,(l_list.val))
                l_list=l_list.next

        dummy = ListNode()
        curr = dummy
        while minheap:
            val = heapq.heappop(minheap)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

class SO_Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []

        # Insert the head of each linked list into the heap
        for i, l_list in enumerate(lists):
            if l_list:
                # Push (node.val, index, node) into the heap
                heapq.heappush(minheap, (l_list.val, i, l_list)) #<-Heap of size k

        # Dummy node to serve as the head of the result list
        dummy = ListNode()
        current = dummy

        # Extract nodes from the heap and build the merged list
        while minheap:
            # Pop the smallest element from the heap (based on node.val)
            val, index, node = heapq.heappop(minheap)

            # Add this node to the merged list
            current.next = node
            current = current.next

            # If there's a next node, push it into the heap
            if node.next:
                heapq.heappush(minheap, (node.next.val, index, node.next))

        # Return the merged linked list
        return dummy.next
