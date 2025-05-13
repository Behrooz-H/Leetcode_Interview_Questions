"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):
            if not node:
                return
            else:
                if len(self.res) == level:
                    self.res.append(node.val)
                    if node.right:
                        dfs(node.right, level + 1)
                    if node.left:
                        dfs(node.left, level + 1)
            return

        dfs(root, 0)
        return self.res
