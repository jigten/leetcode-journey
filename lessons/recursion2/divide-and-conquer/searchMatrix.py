from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def divide(matrix):
        if all([x == [] for x in matrix]):
            return False
        rows = len(matrix)
        pivot = len(matrix[0]) // 2

        i, found = 0, False
        for j in range(rows):
            if (matrix[j][pivot]) == target:
                return True
            if (matrix[j][pivot]) > target:
                i = j
                found = True
                break
        if i == 0 and not found:
            i = rows - 1
        return divide([x[pivot + 1 :] for x in matrix[: i + 1]]) or divide(
            [x[:pivot] for x in matrix[i:]]
        )

    return divide(matrix)


if __name__ == "__main__":
    print(
        searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
        )
    )
    print(
        searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
        )
    )
    print(searchMatrix([[-5]], -2))
    print(searchMatrix([[-1, 3]], -1))
    print(
        searchMatrix(
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            25,
        )
    )
    print(
        searchMatrix(
            [
                [4, 5, 10, 15, 19, 20, 20],
                [4, 9, 12, 15, 22, 23, 26],
                [7, 11, 12, 20, 25, 27, 27],
                [10, 14, 17, 23, 27, 30, 32],
                [11, 18, 19, 24, 28, 34, 39],
            ],
            25,
        )
    )
