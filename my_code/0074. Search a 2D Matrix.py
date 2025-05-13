"""
74. Search a 2D Matrix [Medium]
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

from collections import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0 :
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            mid_idx = (left + right) // 2
            mid_element = matrix[mid_idx // n][mid_idx % n]
            if target == mid_element:
                return True
            else:
                if target < mid_element:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
        return False
    
"""
Time = O(Log(M*N))
Space = O(1)
"""
