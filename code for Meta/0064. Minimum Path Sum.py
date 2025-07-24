"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

"""
import typing
from typing import List

class Solution:
    def __init__(self):
        self.dct ={}

    def fun(self, m ,n):
        if m==0 and n==0: return self.grid[0][0]
        # if (m,n) not in self.dct:
        #     self.dct[(m,n)]= self.fun(m,n)
        elif m==0 and n!=0:
            # if (m, n - 1) not in self.dct:
            #     self.dct[(m, n - 1)] = self.fun(m, n - 1)
            return self.grid[m][n] + self.fun(m,n-1)
        elif n==0 and m!=0 :
            # if (m-1, n) not in self.dct:
            #     self.dct[(m-1, 0)] = self.fun(m-1, n)
            return self.grid[m][n] + self.fun(m-1,n)
        else :
            return self.grid[m][n] + min(self.fun(m-1,n),  self.fun(m,n-1))

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        col = len(grid[0])-1
        row = len(grid)-1
        return self.fun(row,col)


if __name__=="__main__":
    # grid = [[1, 3], [1, 5,]]
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    a=Solution()
    print(a.minPathSum(grid))
