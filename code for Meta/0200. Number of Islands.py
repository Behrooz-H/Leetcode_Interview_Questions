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




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = 0  # mark as visited
                    neighbors = []
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.pop(0)
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"
                        if row + 1 < nr and grid[row + 1][col] == "1":
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = "0"
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = "0"
                        if col + 1 < nc and grid[row][col + 1] == "1":
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"
        return num_islands




if __name__=="__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol=Solution()
    print(sol.numIslands(grid))




