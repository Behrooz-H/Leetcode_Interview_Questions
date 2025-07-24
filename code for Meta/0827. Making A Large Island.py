"""
827. Making A Large Island
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

     
    """
    
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_size = {}
        
        def dfs(x, y, id):
            size = 1
            grid[x][y] = id
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    size += dfs(nx, ny, id)
            return size
        
        # First pass: label islands and record their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_size[island_id] = size
                    island_id += 1
        
        # If the entire grid is 1s
        if not island_size:
            return 1
        
        max_island = max(island_size.values())

        # Second pass: try flipping each 0 and check neighboring islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    new_size = 1
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            id = grid[ni][nj]
                            if id not in seen:
                                new_size += island_size[id]
                                seen.add(id)
                    max_island = max(max_island, new_size)

        return max_island


""" 
⏱ Time Complexity:
First DFS pass (labeling): O(n^2)

Second pass (checking 0s and neighbors): O(n^2)

Each neighbor check per cell is bounded by 4 directions.

Total Time Complexity: O(n^2)

📦 Space Complexity:
O(n^2) for:

storing island sizes

recursion stack (in worst case)

modifying the input grid in-place (no extra grid used)
"""