"""
This code only assumes immediate children of a node but not the entire tree

if root is None:
    return
if root.left is not None:
    if root.left.val >= root.val:
        return False
    self.isValidBST(root.left)
if root.right is not None:
    if root.right.val <= root.val:
        return False
    self.isValidBST(root.right)
return True

To solve it, we need to identify the range of values each node can be in and propogate it accordingly
So, I will have (-inf,+inf) as range in root node
-> Left child will pick (-inf,root.val)
and right child will pick (root.val,inf)

We will update the ranges in each child accordingly and any node violates return False
=> Check left subtree AND check right subtree  --> Answer.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #HAVE A RANGE of VALUES
        def validate(node, min_val, max_val):
            if node is None:
                return True

            # The current node's value must be between min_val and max_val
            if not (min_val < node.val < max_val):
                return False

            # Recursively check the left and right subtree
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        # Initially, there is no min or max constraint, so we use -infinity and infinity
        return validate(root, float('-inf'), float('inf'))
