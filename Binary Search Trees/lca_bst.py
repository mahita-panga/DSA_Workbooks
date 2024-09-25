"""
LCA in a BST
-> We can cash on the property of BST here
-> Combine recursion and backtracking to find the lca
-> whenever we identify that that root,val == p.val or root.val==q.val:
   return that node
-> In case we have empty left subtree, return right value and vice versa and
in case both left and right are empty, return root
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root ==q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        #if left subtree is empty, return right node's value
        if not left:
            return right
        elif not right:
            return left
        else:
            return root

#Easy approach
class EasySolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val < root.val and q.val < root.val: #if both values are in left subtree, explore left
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val: #if both values are in right subtree, explore right
            return self.lowestCommonAncestor(root.right, p, q)

        return root #if one is in left or other is in right, return right
