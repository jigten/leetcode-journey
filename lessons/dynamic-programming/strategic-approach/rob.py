from typing import List


def rob(nums: List[int]) -> int:
    # memo = {}

    # def dp(i):
    #     # Base cases
    #     if i == 0:
    #         return nums[0]
    #     if i == 1:
    #         return max(nums[0], nums[1])
    #     if i not in memo:
    #         memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])  # Recurrence relation
    #         return memo[i]

    # return dp(len(nums) - 1)
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
    print(rob([0]))
