"""
701. Insert into a Binary Search Tree
Insert Given Node to BST
-> Check if val should be in left or right
-> Insert it into the required leaf node

Note: Inserting is better to be done at leaf node level rather than rebalancing the tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        if val<root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        return root
