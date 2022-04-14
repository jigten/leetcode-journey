from functools import lru_cache
from typing import List


def maximumScore(nums: List[int], multipliers: List[int]) -> int:
    n, m = len(nums), len(multipliers)
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for left in range(i, -1, -1):
            mul = multipliers[i]
            right = n - 1 - (i - left)
            dp[i][left] = max(
                (mul * nums[left]) + dp[i + 1][left + 1],
                (mul * nums[right]) + dp[i + 1][left],
            )
    return dp[0][0]


def maximumScoreRecursive(self, nums: List[int], multipliers: List[int]) -> int:
    @lru_cache(2000)
    def dp(i, left):
        # Base case
        if i == m:
            return 0

        mult = multipliers[i]
        right = n - 1 - (i - left)

        # Recurrence relation
        return max(
            mult * nums[left] + dp(i + 1, left + 1),
            mult * nums[right] + dp(i + 1, left),
        )

    n, m = len(nums), len(multipliers)
    return dp(0, 0)


if __name__ == "__main__":
    print(maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
    print(maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
