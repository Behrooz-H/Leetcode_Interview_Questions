"""
994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1

"""
from typing import List


class Solution:
    @staticmethod
    def orangesRotting(grid: List[List[int]]) -> int:
        row_length, col_length, minutes = len(grid), len(grid[0] if grid else 0), 0
        q, fresh_count = [], 0

        def rotten(row, col):
            nonlocal fresh_count
            for r, c in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if -1 < row + r < row_length and -1 < col + c < col_length and grid[row + r][col + c] == 1:
                    grid[row + r][col + c] = 2
                    q.append((row + r, col + c))
                    fresh_count -= 1
            pass

        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1
        lq = len(q)
        minutes = 0
        if not q and fresh_count==0:
            return 0
        if not q and fresh_count>0:
            return -1
        while q:
            while lq > 0:
                row, col = q.pop(0)
                rotten(row, col)
                lq -= 1
            minutes += 1
            lq=len(q)
        return minutes-1 if fresh_count == 0 else -1


if __name__ == "__main__":
    grid = [[1],[2],[1],[2]]
    s = Solution()
    print(s.orangesRotting(grid))
