from collections import defaultdict
from typing import List


def getRow(rowIndex: int) -> List[int]:
    res = []
    seen = defaultdict(int)

    def helper(row, col):
        if col == 0 or row == col:
            return 1

        if (row, col) in seen:
            return seen[(row, col)]
        else:
            seen[(row, col)] = helper(row - 1, col - 1) + helper(row - 1, col)
            return seen[(row, col)]

    col = 0
    while col <= rowIndex:
        res.append(helper(rowIndex, col))
        col += 1

    return res


if __name__ == "__main__":
    print(getRow(24))
