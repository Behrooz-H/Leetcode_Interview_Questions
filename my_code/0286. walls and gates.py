"""
0286 walls and gates You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
FInd the shortest path from each node to the gates and walls will block the access.

"""
class Solution:
    def find_shortest(self, grid):
        q,num_count = [], 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]=="gate":
                    grid[row][col]=0
                    q.append(grid[row][col])
                if grid[row][col] == "inf":
                    num_count+=1
        """
        from each gate start and traverse to each node, if the number achieved so far is smaller than the existing 
        value then update the current value with the smallest value. 
        """
        def update_neighbors(r,c,p):
            for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if -1<r+i<len(grid) and -1<c+j<len(grid[0] if grid else 0):
                    if grid[r+i][c+j] not in ["wall","gate"]:
                        grid[r + i][c + j] = grid[r][c]+1 if (grid[r + i][c + j] !="inf" and grid[r][c]+1 < grid[r + i][c + j]) or grid[r][c] =="inf" else grid[r + i][c + j]
                        p.append((r+i,c+j))

            pass
        while q:
            row , col = q.pop(0)
            p=[(row,col)]
            while p:
                row, col= p.pop(0)
                update_neighbors(row, col,p)



"""
Time complexity : O(mn).

If you are having difficulty to derive the time complexity, start simple.

Let us start with the case with only one gate. The breadth-first search takes at most m×n steps to reach all rooms, therefore the time complexity is O(mn). But what if you are doing breadth-first search from k gates?

Once we set a room's distance, we are basically marking it as visited, which means each room is visited at most once. Therefore, the time complexity does not depend on the number of gates and is O(mn).

Space complexity : O(mn).
The space complexity depends on the queue's size. We insert at most m×n points into the queue.
            """