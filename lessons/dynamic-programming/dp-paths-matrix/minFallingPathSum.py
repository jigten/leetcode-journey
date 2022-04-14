from typing import List


def minFallingPathSum(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    for row in range(1, m):
        for col in range(n):
            if col == 0:
                matrix[row][col] += min(matrix[row - 1][col], matrix[row - 1][col + 1])
            if 0 < col < n - 1:
                matrix[row][col] += min(
                    matrix[row - 1][col - 1],
                    matrix[row - 1][col],
                    matrix[row - 1][col + 1],
                )
            if col == n - 1:
                matrix[row][col] += min(matrix[row - 1][col], matrix[row - 1][col - 1])
    return min(matrix[m - 1])


if __name__ == "__main__":
    print(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(minFallingPathSum([[-19, 57], [-40, -5]]))
    print(minFallingPathSum([[17, 82], [1, -44]]))
