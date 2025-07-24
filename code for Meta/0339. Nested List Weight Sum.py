"""
0339. Nested List Weight Sum

You are given a nested list of integers nestedList. 
Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. 
For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.


"""


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)

"""
Time complexity : O(N). Recursive functions can be a bit tricky to analyze, 
particularly when their implementation includes a loop. A good strategy is to start by determining how many times the recursive function is called, 
and then how many times the loop will iterate across all calls to the recursive function.

The recursive function, dfs(...) is called exactly once for each nested list. As N also includes nested integers, 
we know that the number of recursive calls has to be less than N.
Space complexity : O(N).            
            """
            
            
#BFS Breadth First Search

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)

        depth = 1
        total = 0

        while len(queue) > 0:
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extendleft(nested.getList())
            depth += 1

        return total