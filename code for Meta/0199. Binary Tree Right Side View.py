"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
from typing import List, Optional

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside
"""
Time complexity: O(N) since one has to visit each node.
Space complexity: O(H) to keep the recursion stack, where H is a tree height. 
    The worst-case situation is a skewed tree when H=N.
"""





""" 
Algorithm

Initiate the list of the right side view rightside.

Initiate the queue by adding a root.

While the queue is not empty:

Write down the length of the current level: levelLength = queue.size().

Iterate over i from 0 to level_length - 1:

Pop the current node from the queue: node = queue.poll().

If i == levelLength - 1, then it's the last node in the current level, push it to rightsize list.

Add first left and then right child node into the queue.

Return rightside.
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = deque(
            [
                root,
            ]
        )
        rightside = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                # if it's the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)

                # add child nodes in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside