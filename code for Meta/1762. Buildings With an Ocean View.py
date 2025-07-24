"""
1762. Buildings With an Ocean View
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 
"""
#1st Solution
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        max_height=float("-inf")
        result=[]
        for index in range(len(heights)-1,-1,-1):
            if heights[index]>max_height:
                result=[index]+result
                max_height= heights[index]
        return result

"""
Time  = O(N) Linear search
Space = O(N) The result in worst case scenario can grow to maximum of N size if the originl array is sorted in a decreasing order 
"""
#2nd solution
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []

        for current in range(n):
            # If the current building is taller, 
            # it will block the shorter building's ocean view to its left.
            # So we pop all the shorter buildings that have been added before.
            while answer and heights[answer[-1]] <= heights[current]:
                answer.pop()
            answer.append(current)
            
        return answer



#3rd Solution
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        max_height=float("-inf")
        result=[]
        for index in range(len(heights)-1,-1,-1):
            if heights[index]>max_height:
                result=[index]+result
            max_height=max(max_height, heights[index])
        return result
    
    
#Monotonic Stack Approach    
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []
        
        # Monotonically decreasing stack.
        stack = []
        for current in reversed(range(n)):
            # If the building to the right is smaller, we can pop it.
            while stack and heights[stack[-1]] < heights[current]:
                stack.pop()
            
            # If the stack is empty, it means there is no building to the right 
            # that can block the view of the current building.
            if not stack:
                answer.append(current)
            
            # Push the current building in the stack.
            stack.append(current)
        
        answer.reverse()
        return answer