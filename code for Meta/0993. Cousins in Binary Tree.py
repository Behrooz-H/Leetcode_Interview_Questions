"""
993. Cousins in Binary Tree
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Nones
from collections import defaultdict
class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # Queue for BFS
        queue = collections.deque([root])

        while queue:

            siblings = False
            cousins = False
            nodes_at_depth = len(queue)
            for _ in range(nodes_at_depth):

                # FIFO
                node = queue.popleft()  

                # Encountered the marker.
                # Siblings should be set to false as we are crossing the boundary.
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        # Set both the siblings and cousins flag to true
                        # for a potential first sibling/cousin found.
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            # If the siblings flag is still true this means we are still
                            # within the siblings boundary and hence the nodes are not cousins.
                            return not siblings

                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    # Adding the null marker for the siblings
                    queue.append(None)
            # After the end of a level if `cousins` is set to true
            # This means we found only one node at this level
            if cousins:
                return False

        return False 
    
"""
Time Complexity: O(N), where N is the number of nodes in the binary tree. 
In the worst case, we might have to visit all the nodes of the binary tree. Similar to approach 1 this approach would also have a complexity of O(N) when the Node x and Node y are present at the last level of the binary tree. The algorithm would follow the standard BFS approach and end up in checking each node before discovering the desired nodes.

Space Complexity: O(N). In the worst case, we need to store all the nodes of the last level in the queue. The last level of a binary tree can have a maximum of  
2
N nodes. Not to forget we would also need space for  
4
N
null markers, one for each pair of siblings. That results in a space complexity of O( 
4
3N) = O(N) (You are right Big-O notation doesn't care about constants)."""