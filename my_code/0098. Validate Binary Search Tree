"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def valid_ancestors(self,root, max_par, min_par):
        if root:
            if root.val<=min_par or root.val>=max_par:
                return False
            if not self.valid_ancestors(root.right,max_par,root.val):
                return False
            if not self.valid_ancestors(root.left, root.val, min_par):
                return False
            return True
        else:
            return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_par = float("inf")
        min_par = float("-inf")
        return self.valid_ancestors(root, max_par, min_par)


if __name__=="__main__":
    # a=[5, 1, 4, None, None, 3, 6]
    d =TreeNode(0,right=TreeNode(-1))
    sol = Solution()
    print(sol.isValidBST(d))
