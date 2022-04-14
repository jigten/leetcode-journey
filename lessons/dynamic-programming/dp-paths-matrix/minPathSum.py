from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if row > 0 and col == 0:
                grid[row][col] += grid[row - 1][col]
            elif col > 0 and row == 0:
                grid[row][col] += grid[row][col - 1]
            elif row > 0 and col > 0:
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
    return grid[m - 1][n - 1]


if __name__ == "__main__":
    print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(minPathSum([[1, 2, 3], [4, 5, 6]]))
