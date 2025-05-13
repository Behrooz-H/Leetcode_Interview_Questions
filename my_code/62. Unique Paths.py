
"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
# Math Only using Factorial
# Time complexity:O((M+N)(log(M+N)loglog(M+N))^2).
# Space complexity: O(1).

from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)



# Time: O(N*M)
# Space complexity: O(N×M) for the matrix
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]



# ** Memoization plus  without memoization it will be 2^m+n and noe=w it is m+n
class Solution:
    def __init__(self):
        self.dct = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        elif m == 1 and n == 1:
            return 1
        else:
            if (m - 1, n) not in self.dct:
                self.dct[(m - 1, n)] = self.uniquePaths(m - 1, n)
            sub_m = self.dct[(m - 1, n)]
            if (m, n - 1) not in self.dct:
                self.dct[(m, n - 1)] = self.uniquePaths(m, n - 1)
            sub_n = self.dct[(m, n - 1)]
            return sub_m + sub_n
