"""
298. Binary Tree Longest Consecutive Sequence

Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is a path where the values increase by one along the path.

Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent=None, length=0) -> int:
            if not node:
                return length
            length = length+1 if parent and parent.val+1== node.val else 1
            return max(length, dfs(node.left,node, length),dfs(node.right,node, length))
        return dfs(root, length=0)
