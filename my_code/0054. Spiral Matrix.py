"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""
from typing import List

# Time complexity: O(M*N) == O(row_size*column_size)
#Space Complexity : O(1)

class Solution:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result








class Week_solution:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        arrow, count, r, c, row_low, col_low, row_up, col_up = 0, 0, 0, 0, -1, -1, len(matrix), len(
                matrix[0]) if matrix else 0
        mat_size = row_up * col_up
        order, q, correct = [(0, 1), (1, 0), (0, -1), (-1, 0)], [], [(1, 0, 0, 0), (0, 0, 0, -1), (0, -1, 0, 0),
                                                                     (0, 0, 1, 0)]

        def move(r, c, direct, correct):
            nonlocal row_low, row_up, col_low, col_up
            while row_low < r < row_up and col_low < c < col_up and len(q) < mat_size:
                q.append(matrix[r][c])
                r += direct[0]
                c += direct[1]
            r -= direct[0]
            c -= direct[1]
            row_low += correct[0]
            row_up += correct[1]
            col_low += correct[2]
            col_up += correct[3]
            return r, c

        while row_low < r < row_up and col_low < c < col_up and len(q) < mat_size:
            r, c = move(r, c, order[arrow % 4], correct[arrow % 4])
            arrow += 1
            r += order[arrow % 4][0]
            c += order[arrow % 4][1]
        return q


if __name__ == "__main__":
    sol = Week_solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(mat))
