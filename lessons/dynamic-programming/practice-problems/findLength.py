from functools import lru_cache
from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    m, n = len(nums1), len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    maxlen = 0
    for i in range(m):
        for j in range(n):
            if nums1[i] == nums2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
                maxlen = max(maxlen, dp[i + 1][j + 1])
    return maxlen


if __name__ == "__main__":
    print(findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
    print(findLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0]))
