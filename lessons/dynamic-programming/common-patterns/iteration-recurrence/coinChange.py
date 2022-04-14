from functools import lru_cache
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # @lru_cache(None)
    # def dp(i):
    #     if i == 0:
    #         return 0
    #     best = float("inf")
    #     for c in coins:
    #         if c <= i:
    #             best = min(best, dp(i - c) + 1)
    #     return best

    # ans = dp(amount)
    # return ans if ans != float("inf") else -1
    if amount == 0:
        return 0
    dp = [float("inf")] * amount
    dp[0] = 0
    for i in range(1, amount):
        best = float("inf")
        for c in coins:
            if c <= i:
                best = min(best, dp[i - c] + 1)
        dp[i] = best
    ans = dp[amount - 1]
    return ans if ans != float("inf") else -1


if __name__ == "__main__":
    print(coinChange(coins=[1, 2, 3], amount=10))
    print(coinChange(coins=[2], amount=3))
    print(coinChange(coins=[1], amount=0))
