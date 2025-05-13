"""
48. Rotate Image
-------------------
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
==================================================
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""
#
# Time complexity : \mathcal{O}(M)O(M). We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a cost of \mathcal{O}(M)O(M) because we're moving the value of each cell once. Reversing each row also has a cost of \mathcal{O}(M)O(M), because again we're moving the value of each cell once.
#
# Space complexity : \mathcal{O}(1)O(1) because we do not use any other additional data structures.
from typing import List
class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose():
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        def reflect():
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
        transpose()
        reflect()
