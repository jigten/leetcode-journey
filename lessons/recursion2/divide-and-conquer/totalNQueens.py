import copy
from collections import defaultdict


class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for _ in range(n)] for _ in range(n)]
        self.total = 0
        self.PlaceQ(board, 0, n)

        return self.total

    def PlaceQ(self, board, r, n):
        if r == n:
            self.total += 1
            return
        for i in range(n):
            if self.checkPlace(board, n, r - 1, i):
                board[r][i] = "Q"
                new = copy.deepcopy(board)
                self.PlaceQ(new, r + 1, n)
                board[r][i] = "."

    def checkPlace(self, board, n, r, c):
        i = r
        j = c - 1
        k = c + 1
        while i >= 0:
            if board[i][c] == "Q":
                return False
            if j >= 0 and board[i][j] == "Q":
                return False
            if k < n and board[i][k] == "Q":
                return False
            i -= 1
            j -= 1
            k += 1
        return True


if __name__ == "__main__":
    print(Solution().totalNQueens(4))
    # print(totalNQueens(1))
