from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    if n == 1:
        return cost[0]

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])


if __name__ == "__main__":
    print(minCostClimbingStairs([10, 15, 20]))
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(minCostClimbingStairs([1]))
