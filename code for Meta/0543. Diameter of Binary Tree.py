"""
0543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return -1
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path + 2)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter
    
""" 
Time complexity: O(N). This is because in our recursion function longestPath, we only enter and exit from each node once. 
We know this because each node is entered from its parent, and in a tree, nodes only have one parent.

Space complexity: O(N). The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. 
In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(logN).
"""









""" 
Time complexity: O(N). This is because in our recursion function longestPath, we only enter and exit from each node once.
We know this because each node is entered from its parent, and in a tree, nodes only have one parent.
Space complexity: O(N). The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree.
In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(logN).
"""