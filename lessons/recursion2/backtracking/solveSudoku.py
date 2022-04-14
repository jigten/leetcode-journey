import copy
from typing import List


def solveSudoku(board: List[List[str]]) -> None:
    n = len(board)

    def isValid(board, candidate, row, col, n):
        if any([candidate == x for x in board[row]]):
            return False

        for i in range(n):
            if candidate == board[i][col]:
                return False

        return True

    def solver(board, r, c, n):
        if c == n:
            return
        for candidate in range(1, 10):
            if isValid(board, candidate, r, c, n):
                board[i][c] = candidate
                new = copy.deepcopy(board)
                solver(new, r, c + 1, n)
                board[i][c] = "."

    for i in range(n):
        if i == n:
            return
        solver(board, i, 0, n)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        assert self.backtrack(board, 0, 0)
        return

    def backtrack(self, board: List[List[str]], r: int, c: int) -> bool:
        # Go to next empty space
        while board[r][c] != ".":
            c += 1
            if c == 9:
                c, r = 0, r + 1
            if r == 9:
                return True
        # Try all options, backtracking if not work
        for k in range(1, 10):
            if self.isValidSudokuMove(board, r, c, str(k)):
                board[r][c] = str(k)
                if self.backtrack(board, r, c):
                    return True
        board[r][c] = "."
        return False

    def isValidSudokuMove(
        self, board: List[List[str]], r: int, c: int, cand: int
    ) -> bool:
        # Check row
        if any(board[r][j] == cand for j in range(9)):
            return False
        # Check col
        if any(board[i][c] == cand for i in range(9)):
            return False
        # Check block
        br, bc = 3 * (r // 3), 3 * (c // 3)
        if any(
            board[i][j] == cand for i in range(br, br + 3) for j in range(bc, bc + 3)
        ):
            return False
        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solveSudoku(board)
    print(board)
