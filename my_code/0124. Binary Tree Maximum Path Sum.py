"""
0124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
 
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float("inf")

        # post order traversal of subtree rooted at `node`
        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath

            if not node:
                return 0

            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gainFromLeft = max(gainFromSubtree(node.left), 0)

            # add the gain / path sum from right subtree. 0 if negative
            gainFromRight = max(gainFromSubtree(node.right), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)

            # return the max sum for a path starting at the root of subtree
            return max(gainFromLeft + node.val, gainFromRight + node.val)

        gainFromSubtree(root)
        return maxPath
    
    
    
"""
Time complexity: O(n)

Each node in the tree is visited only once. During a visit, we perform constant time operations, including two recursive calls and calculating the max path sum for the current node. So the time complexity is O(n).

Space complexity: O(n)

We don't use any auxiliary data structure, but the recursive call stack can go as deep as the tree's height. In the worst case, the tree is a linked list, so the height is n. Therefore, the space complexity is O(n).

"""