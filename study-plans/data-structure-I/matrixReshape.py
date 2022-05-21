from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat

    res = [[0] * c for _ in range(r)]
    i, j = 0, 0
    for rVal in mat:
        for cVal in rVal:
            if j == c:
                i += 1
                j = 0
            res[i][j] = cVal
            j += 1
    return res

print(matrixReshape([[1,2],[3,4]], 1, 4))
print(matrixReshape([[1,2],[3,4]], 2, 4))
print(matrixReshape([[1,2],[3,4]], 4, 1))
