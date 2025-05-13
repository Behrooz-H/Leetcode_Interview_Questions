"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(i, j):
            return True if 0 <= i < len_row and 0 <= j < len_col and grid[i][j] == "1" else False
        len_row, len_col,island_count= len(grid), len(grid[0]if grid[0] else 0),0
        for row in range(len_row):
            for col in range(len_col):
                if is_valid(row, col):
                    island_count += 1
                    q = [(row, col)]
                    while q:
                        r, c = q.pop()
                        if grid[r][c] == "1":
                            grid[r][c] = "0"
                            for r_move, c_move in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                                if is_valid(r + r_move, c + c_move):
                                    q.append((r + r_move, c + c_move))
        return island_count

if __name__=="__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol=Solution()
    print(sol.numIslands(grid))
