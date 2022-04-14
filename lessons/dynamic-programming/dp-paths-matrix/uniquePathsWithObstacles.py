from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    obstacleGrid[0][0] = 2 if obstacleGrid[0][0] != 1 else 0

    for row in range(m):
        for col in range(n):
            top, left = obstacleGrid[row - 1][col], obstacleGrid[row][col - 1]
            if obstacleGrid[row][col] == 1:
                continue
            if row > 0:
                obstacleGrid[row][col] += top if top != 1 else 0
            if col > 0:
                obstacleGrid[row][col] += left if left != 1 else 0

    return int(obstacleGrid[m - 1][n - 1] / 2)


if __name__ == "__main__":
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles([[0, 1], [0, 0]]))
    print(uniquePathsWithObstacles([[0]]))
    print(uniquePathsWithObstacles([[1]]))
