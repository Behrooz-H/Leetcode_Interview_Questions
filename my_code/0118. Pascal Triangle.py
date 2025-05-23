"""
0118. Pascal Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle
    
    # O(n^2)
"""
Time complexity: O(numRows ^2)
Although updating each value of triangle happens in constant time, it
is performed O(numRows2 ) times. To see why, consider how many
overall loop iterations there are. The outer loop obviously runs
numRows times, but for each iteration of the outer loop, the inner
loop runs rowNum times. Therefore, the overall number of triangle updates
that occur is 1+2+3+…+numRows, which, according to Gauss' formula

Space complexity: O(1)
While O(numRows^2) space is used to store the output, the input and output generally do not count towards 
the space complexity.
"""