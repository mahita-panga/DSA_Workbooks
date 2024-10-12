"""
846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
SIMILAR TO  https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Note: Numbers in a group should be consecutive.

Intuition:
-> Split the list hand into groups of size groupSize, where each group consists of consecutive integers.
->  Count occurrences of each card using a Counter.
    Use a min-heap to keep track of the smallest card available (since the heap gives the smallest element efficiently).
	For each group, try to take the smallest card and the next consecutive cards, reducing their counts in the Counter.
	Return False if any card needed for the group is missing.
-> After using a card, reduce its count and remove it from the heap when its count becomes zero.

TC:  O(nlog k), where n is the number of cards and k is the number of unique cards.
SC: O(k), where k is the number of unique cards.
"""
import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        # If we can't divide the hand into groups of 'groupSize', return False
        if n % groupSize != 0:
            return False

        # Count the occurrences of each card
        count_map = Counter(hand)

        # Create a min-heap of unique cards (based on keys of the Counter)
        min_heap = list(count_map.keys())
        heapq.heapify(min_heap)

        # Try to form consecutive groups of size 'groupSize'
        while min_heap:
            first_card = min_heap[0]  # Get the smallest card

            # Try to form a group starting from 'first_card'
            for i in range(groupSize):
                current_card = first_card + i

                # If the current card is missing from the hand, return False
                if count_map[current_card] == 0:
                    return False

                # Decrease the count of the current card in the hand
                count_map[current_card] -= 1

                # If the count becomes zero, remove it from the heap
                if count_map[current_card] == 0:
                    # If the card was the smallest in the heap, pop it
                    if current_card == min_heap[0]:
                        heapq.heappop(min_heap)
                    else:
                        del count_map[current_card]

        return True
