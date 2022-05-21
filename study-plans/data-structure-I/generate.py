from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = [[0] * m for m in range(1, numRows + 1)]
    r, c, res[0][0] = 1, 0, 1
    
    for r in range(1, numRows):
        for c in range(r + 1):
            if c == 0 or c == r:
                res[r][c] = 1
            else:
                res[r][c] = res[r - 1][c - 1] + res[r - 1][c]
    return res

print(generate(5))
print(generate(1))
