"""

1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1 
        
        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
        
        # There was no path.
        return -1
    
"""
Let N be the number of cells in the grid.

Time complexity : O(N).
Each cell was guaranteed to be enqueued at most once. 
This is because a condition for a cell to be enqueued was that it had a zero in the grid,
and when enqueuing, we also permanently changed the cell's grid value to be non-zero.
The outer loop ran as long as there were still cells in the queue, dequeuing one each time. 
Therefore, it ran at most N times, giving a time complexity of O(N).
The inner loop iterated over the unvisited neighbors of the cell that was dequeued by the outer loop.
There were at most 8 neighbors. 
Identifying the unvisited neighbors is an O(1) operation because we treat the 8 as a constant.
Therefore, we have a time complexity of O(N).

Space complexity : O(N).
The only additional space we used was the queue. We determined above that at most, we enqueued N cells. Therefore, an upper bound on the worst-case space complexity is O(N).
Given that BFS will have nodes of at most two unique distances on the queue at any one time, it would be reasonable to wonder if the worst-case space complexity is actually lower. But actually, it turns out that there are cases with massive grids where the number of cells at a single distance is proportional to N. So even with cells of a single distance on the queue, in the worst case, the space needed is O(N).

"""