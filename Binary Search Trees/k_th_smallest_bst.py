"""
-> Do inorder traversal
-> Keep a cntr
-> In inorder traversal, once you reach the left node or smallest element
return that kth element.

Note : Make sure cntr is a nonlocal variable or define it accordingly in the method.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0  # Initialize cnt here

        def inorder(root):
            nonlocal cnt
            if root is None:
                return None

            # Traverse the left subtree
            left = inorder(root.left)
            if left is not None:
                return left

            # Increment cnt when visiting the node
            cnt += 1
            if cnt == k:
                return root.val

            # Traverse the right subtree
            return inorder(root.right)

        return inorder(root)
