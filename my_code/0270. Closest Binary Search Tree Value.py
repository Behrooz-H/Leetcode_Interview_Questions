""" 
270. Closest Binary Search Tree Value
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.
"""



class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        return closest
"""
time= O(h) --> tree Height       
Space = O(1)
        """






















#Bad

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def dfs(node, target):
            if not node:
                return float("inf")
            if node.val<target:
                    return min(node.val,dfs(node.right, target), key= lambda x: (abs(target-x),x)) 
            elif node.val>=target:
                    return min (node.val, dfs(node.left, target), key = lambda x: (abs(target-x),x)) 
        return dfs(root, target)
    
"""
Time =  O(N)
Space = O(N) due to recursive function calls
"""