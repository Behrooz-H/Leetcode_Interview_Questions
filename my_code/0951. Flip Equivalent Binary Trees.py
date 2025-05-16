"""951. Flip Equivalent Binary Trees
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise."""



class Solution:
    def flipEquiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        # Both trees are empty
        if not root1 and not root2:
            return True
        # Just one of the trees is empty
        if not root1 or not root2:
            return False
        # Corresponding values differ
        if root1.val != root2.val:
            return False

        # Check if corresponding subtrees are flip equivalent
        no_swap = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )

        # Check if opposite subtrees are flip equivalent
        swap = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(
            root1.right, root2.left
        )

        return no_swap or swap

"""
Time Complexity: O(N).
This is because the recursion stops at the leaf nodes or when a mismatch occurs. 
In the worst case, every node in the smaller tree will be visited.

Space Complexity: O(N).
This is due to the recursion stack. In the worst case, the recursion goes as deep as the tree's height, 
which can be O(N) in the case of a skewed tree (a tree in which every internal node has only one child). 
For a balanced tree, the space complexity will be O(logN) because the tree's height would be logarithmic 
relative to the number of
"""





class Solution:
    def find_canonical_form(self, root: TreeNode) -> None:
        if not root:
            return

        # Post-order traversal: first bring subtrees into their canonical form
        self.find_canonical_form(root.left)
        self.find_canonical_form(root.right)

        if not root.right:
            return

        # Swap subtrees, so that left is non-empty
        if not root.left:
            root.left = root.right
            root.right = None
            return
        left = root.left
        right = root.right

        # Swap subtrees
        if left.val > right.val:
            root.left, root.right = root.right, root.left

    def are_equivalent(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.are_equivalent(
            root1.left, root2.left
        ) and self.are_equivalent(root1.right, root2.right)

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.find_canonical_form(root1)
        self.find_canonical_form(root2)
        return self.are_equivalent(root1, root2)