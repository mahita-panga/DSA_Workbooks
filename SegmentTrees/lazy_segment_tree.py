"""
Lazy propagation is used to efficiently apply range updates. Here’s the updated segment tree class with lazy propagation:

	1.	Lazy Array: We maintain an additional array to keep track of “pending” updates for each node.
	2.	push_down Function: This function ensures that any pending updates at a node are propagated to its children.

"""

class SegTreeNode:
    def __init__(self, val=0):
        self.val = val  # Represents the value stored at this node


# Merge function to combine two nodes based on the operation
def merge(left: SegTreeNode, right: SegTreeNode) -> SegTreeNode:
    node = SegTreeNode()
    node.val = left.val + right.val  # Change this to min/max/XOR for other types of queries
    return node


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [SegTreeNode() for _ in range(4 * self.n)]  # Segment tree array
        self.lazy = [0] * (4 * self.n)  # Lazy array for pending updates
        self.build(1, 0, self.n - 1)  # Build the tree starting with root at index 1

    # Build function to construct the segment tree
    def build(self, idx, start, end):
        if start == end:
            # Leaf node directly takes the array value
            self.tree[idx] = SegTreeNode(self.arr[start])
        else:
            mid = (start + end) // 2
            self.build(2 * idx, start, mid)
            self.build(2 * idx + 1, mid + 1, end)
            self.tree[idx] = merge(self.tree[2 * idx], self.tree[2 * idx + 1])

    # Push down function to propagate lazy updates to children
    def push_down(self, idx, start, end):
        if self.lazy[idx] != 0: #If lazy is not 0 => updates are pending
            # Apply the lazy value to this node
            self.tree[idx].val += (end - start + 1) * self.lazy[idx]  # Adjust for range size if it's a sum

            if start != end:  # If not a leaf, propagate to children
                self.lazy[2 * idx] += self.lazy[idx]
                self.lazy[2 * idx + 1] += self.lazy[idx]

            # Clear the lazy value for this node after propagation
            self.lazy[idx] = 0

    # Range update function with lazy propagation
    def update_range(self, idx, start, end, L, R, value):
        # First, push down any pending updates
        self.push_down(idx, start, end)

        if start > R or end < L:  # No overlap
            return

        if start >= L and end <= R:  # Total overlap => we know all elements in this range needs to updated.
            # Apply the update lazily
            self.lazy[idx] += value
            self.push_down(idx, start, end)  # Push down to update the current node immediately
        else:
            # Partial overlap, propagate the update to children and then update aaram se
            mid = (start + end) // 2
            self.update_range(2 * idx, start, mid, L, R, value)
            self.update_range(2 * idx + 1, mid + 1, end, L, R, value)
            self.tree[idx] = merge(self.tree[2 * idx], self.tree[2 * idx + 1])

    # Range query function with lazy propagation
    def query_range(self, idx, start, end, L, R):
        self.push_down(idx, start, end)  # Ensure all updates are applied before querying

        if start > R or end < L:  # No overlap
            return SegTreeNode(0)  # Identity element for sum; adjust if using min/max

        if start >= L and end <= R:  # Total overlap
            return self.tree[idx]

        # Partial overlap
        mid = (start + end) // 2
        left_result = self.query_range(2 * idx, start, mid, L, R)
        right_result = self.query_range(2 * idx + 1, mid + 1, end, L, R)
        return merge(left_result, right_result)

    # Wrapper methods for ease of use
    def range_update(self, L, R, value):
        self.update_range(1, 0, self.n - 1, L, R, value)

    def range_query(self, L, R):
        return self.query_range(1, 0, self.n - 1, L, R).val


# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Update range [1, 3] by adding 5
seg_tree.range_update(1, 3, 5)

# Query the range sum from index 1 to 4
print(seg_tree.range_query(1, 4))  # Output reflects updated values due to lazy propagation
