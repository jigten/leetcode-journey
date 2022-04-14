from collections import Counter
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    pts = Counter(nums)
    n = max(pts.keys()) + 1
    dp = [0] * n
    dp[0] = 0
    dp[1] = 0 if not pts[1] else pts[1] * 1
    for i in range(2, n):
        curr = pts[i] * i if pts[i] else 0
        dp[i] = max(curr + dp[i - 2], dp[i - 1])
    return dp[n - 1]


if __name__ == "__main__":
    print(deleteAndEarn([3, 4, 2]))
    print(deleteAndEarn([2, 2, 3, 3, 3, 4]))
