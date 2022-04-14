from functools import lru_cache
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)

    @lru_cache(None)
    def dp(i):
        if i == 0:
            return 1
        best = float("-inf")
        for j, num in enumerate(nums[: i + 1]):
            if num < nums[i]:
                best = max(best, 1 + dp(j))

        return best if best != float("-inf") else 1

    ans = float("-inf")
    for i in range(n):
        ans = max(ans, dp(i))

    return ans


if __name__ == "__main__":
    print(lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
