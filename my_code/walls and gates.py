"""
FInd the shortest path from each node to the gates and walls will block the access
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

