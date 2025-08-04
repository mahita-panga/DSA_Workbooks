"""
https://leetcode.com/problems/all-oone-data-structure/description/?envType=problem-list-v2&envId=linked-list

    ## Concept of LRU - HMAP+DLL
    ## As we need O(1) for putting and getting the values -dll

    Here we need keys ordered by freq count i.e freq sortrd dll
    so we need dll of buckets which represents a count nd all strings with that count.
    we have a hmap - key_bucket  which tells which node/bucket key lies in
    we need a count_bucket which tells which count the bucket node falls in
    both these mapps help us to use the same node/bucket for all keys with same count

-->GPT NOTES
We need a data structure that can:
	•	Track counts of string keys
	•	Get max count key and min count key — in O(1) time.

A normal hash map gives us O(1) key-value lookups, but not O(1) for min/max.
To solve this, we combine:
	•	Doubly Linked List (DLL) of buckets (each bucket = 1 unique count).
	•	Each bucket holds keys having that count.
	•	Two hash maps:
	1.	key_bucket: key → node in DLL (bucket where it lives)
	2.	count_bucket: count → node in DLL (bucket with that count)

DLL Structure:
    - Each bucket represents a unique count.
    - Each bucket contains a set of keys with that count.
    - The DLL is ordered by count, with the head representing the minimum count and the tail representing the maximum count.
    - The DLL allows for efficient insertion and removal of buckets.
-- head <-> [count=1, keys: {"a", "b"}] <-> [count=2, keys: {"c"}] <-> tail

inc(key) - key is new, place in count=1 wala bucket
            else: remove from curr bucket and add to +1 wala bucket. if old bucket is empty, delete
dec(key) - Key has cnt 1, remove from the bucket and key_bucket hmap
            else: remove from curr bucket and add to -1 wala bucket. if old bucket is empty, delete
getMaxKey() - tail.prev- buck with max count
getMinKey() - head.next- buck with min count
pick any key from that bucket's key set()

Handle edge cases
"""
from pip._vendor.requests import delete
class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('-inf'))
        self.head.next = self.tail
        self.tail.prev = self.head #head <==>tail

        self.key_count = {}     # key -> Node (which key is in which npde)
        self.count_bucket = {}  # count -> Node (which count is in which node)

    def _add_bucket_after(self, new_bucket, prev_bucket):
        nxt = prev_bucket.next
        prev_bucket.next = new_bucket
        new_bucket.prev = prev_bucket
        new_bucket.next = nxt
        nxt.prev = new_bucket

    def _remove_bucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev
        del self.count_bucket[bucket.count]


    def inc(self, key: str) -> None:
        if key in self.key_count:
            curr_bucket = self.key_count[key]
            new_count = curr_bucket.count + 1
            curr_bucket.keys.remove(key)

            if new_count in self.count_bucket:
                new_bucket = self.count_bucket[new_count]
            else:
                new_bucket = Node(new_count)
                self.count_bucket[new_count] = new_bucket
                self._add_bucket_after(new_bucket, curr_bucket)

            new_bucket.keys.add(key)
            self.key_count[key] = new_bucket

            if not curr_bucket.keys:
                self._remove_bucket(curr_bucket)
        else:
            # New key with count = 1
            if 1 in self.count_bucket:
                bucket = self.count_bucket[1]
            else:
                bucket = Node(1)
                self.count_bucket[1] = bucket
                self._add_bucket_after(bucket, self.head)

            bucket.keys.add(key)
            self.key_count[key] = bucket

    def dec(self, key: str) -> None:
        curr_bucket = self.key_count[key]
        curr_count = curr_bucket.count
        curr_bucket.keys.remove(key)

        if curr_count == 1:
            del self.key_count[key]
        else:
            new_count = curr_count - 1
            if new_count in self.count_bucket:
                new_bucket = self.count_bucket[new_count]
            else:
                new_bucket = Node(new_count)
                self.count_bucket[new_count] = new_bucket
                self._add_bucket_after(new_bucket, curr_bucket.prev)

            new_bucket.keys.add(key)
            self.key_count[key] = new_bucket

        if not curr_bucket.keys:
            self._remove_bucket(curr_bucket)


    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))


    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
