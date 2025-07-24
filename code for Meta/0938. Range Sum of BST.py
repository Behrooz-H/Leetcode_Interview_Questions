"""
938. Range Sum of BST
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0
            left_result= dfs(root.left) if root.left and root.val>low else 0
            right_result= dfs(root.right) if root.right  and root.val<high else 0
            return left_result+right_result+( root.val if low<=root.val<=high else 0)
        return dfs(root)
    
    
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val and node.left:
                    stack.append(node.left)
                if node.val < high and node.right:
                    stack.append(node.right)
        return ans