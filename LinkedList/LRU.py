"""
https://leetcode.com/problems/lru-cache/?envType=problem-list-v2&envId=linked-list

We need a DLL + HMAP to maintain the LRU cache.
DLL - maintains the cache behaviour i.e add the nodes and in case any node is picked/updated,move these references to the top
so to do this we can start with a DLL which has dummy head and dummy tail
head <===> tail
head <==> (MRU) ... <==> (LRU) <==> tail
HMAP maintains the references of key and node i.e node address which will help us check and get the val in dll. this hmap helps us check if ele is present in dll without traversing it.

-> insert_ele_into_dll
    -> insertion happens at head
        insert(2,2)
        head<==> (2,2) <==> tail and update hmap to have {2, Node}
        insert (4,6)
        head<==>(4,6)<==>(2,2)<==>tail and update hmap - {2,Node},{4,Node}
        if hmap size> cache size, delete from tail before inserting

-> delete_ele_from_dll
    -> deletion happens from tail
        delete (2,2) - get Node from hmap
        delet node from dll - head <==>(4,6)<==>tail and also pop this from hmap.

->put - -> if in hmap:
            -> pop from hmap
            -> del from dll
            -> insert into dll at hmap
        -> else;
            insert into hmap
            insert at head
->get - ->if in hmap,
            -> pop from hmap
            -> del from dll
            -> insert into dll at hmap
            -> return val
        else:
            return -1

"""
class Node:
    def __init__(self,key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hmap = {}

        self.head = Node()
        self.tail = Node()

        #empty dll/lru
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_into_cache(self,key,val):
        node = Node(key,val) #  2 <- Node -> T
        #update nod ref.
        node.prev = self.head
        node.next = self.head.next

        #set this node before the head's next node's prev
        self.head.next.prev = node
        #set head's next
        self.head.next = node

        self.hmap[key] = node

    def delete_from_cache(self,key):
        node_val = self.hmap.pop(key)

        prev_node = node_val.prev
        next_node = node_val.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return node_val.val


    def get(self, key: int) -> int:
        if key in self.hmap:
            val = self.delete_from_cache(key)
            self.insert_into_cache(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.delete_from_cache(key)

        self.insert_into_cache(key, value)

        if len(self.hmap) > self.cap: # evict LRU -> first
            self.delete_from_cache(self.tail.prev.key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
