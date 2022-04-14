from typing import List


def maxSubArray(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray([1]))
    print(maxSubArray([5, 4, -1, 7, 8]))
