"""
688. Knight Probability in Chessboard

"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        x_dir = [2, 1, -1, -2, -2, -1, 1, 2]
        y_dir = [1, 2, 2, 1, -1, -2, -2, -1]

        cache = {}

        def kMoves(i, j, moves):
            if i >= n or j >= n or i < 0 or j < 0:
                return 0
            if moves == k:
                return 1
            if (i, j, moves) in cache:
                return cache[(i, j, moves)]
            totMoves = 0
            for ind in range(8):
                totMoves += kMoves(i + x_dir[ind], j + y_dir[ind], moves + 1) * (1 / 8)

            cache[(i, j, moves)] = totMoves
            return totMoves

        return kMoves(row, column, 0)


class Week_solution:
    # Knight valid directions are various 8 distinct
    dct= {}
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if row<0 or row>=n or column<0 or column>=n or n==0:
            return 0
        if k==0:
            return 1
        if (row, column, k) not in self.dct:
            return self.dct[(row, column, k)]
        res = 0
        for r,c in [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (-2,-1), (2,-1)]:
            res+=self.knightProbability(n, k-1, row+r, column+c)/8
        self.dct[(row, column, k)] = res
        return res



if __name__=="__main__":
    sol=Solution()
    print(sol.knightProbability(8,2,3,4))
