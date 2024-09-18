"""
Given a BST, find ceil of a number.
-> If number is present then return number else the number just > this number

-> Take a variable ceil = -1
-> Until root is None: //traverse the tree
    if val found, just update the ceil and return
    if val is probably on the left side, then update ceil to the root node
    //Is done under assumption that if ceil is not found, this will the ceil to the number
    If vale is on right side, then just search the right
-> return ceil
"""

class Solution:
    def findCeil(self,root, inp):
        # code here
        ceil = -1
        while root:
            if root.key == inp:
                ceil = inp
                break
            if inp>root.key:
                root = root.right
            else:
                ceil = root.key
                root = root.left

        return ceil


"""
FLOOR -> BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
"""
class Solution:
    def floor(self, root, x):
        # Code here
        floor = -1
        while root:
            if root.data == x:
                floor = root.data
                break
            if x < root.data:
                root = root.left
            else:
                floor = root.data
                root = root.right


        return floor
