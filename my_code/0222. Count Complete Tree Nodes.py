"""
222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
 and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity
"""

from typing import Optional
from math import ceil


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def get_tree_height(root):
        height = 0
        while root.left:
            height += 1
            root = root.left
        return height

    @staticmethod
    def node_exist(index_to_find: int, height: int, node):
        count, left, right = 0, 0, 2 ** height - 1
        while count < height:
            mid_node = ceil((left + right) / 2)
            if index_to_find >= mid_node:
                node = node.right
                left = mid_node
            else:
                node = node.left
                right = mid_node - 1
            count += 1
        return True if node else False

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        height = self.get_tree_height(root)
        if height == 0:
            return 1
        upper_count = 2 ** height - 1
        left, right = 0, upper_count
        while left < right:
            # binary search fo rthe last level
            index_to_find = ceil((left + right) / 2)
            if self.node_exist(index_to_find, height, root):
                left = index_to_find
            else:
                right = index_to_find - 1

        return upper_count + left + 1
