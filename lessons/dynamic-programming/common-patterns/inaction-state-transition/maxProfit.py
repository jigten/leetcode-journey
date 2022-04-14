from functools import lru_cache
from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    @lru_cache(None)
    def dp(i, k, holding):
        if i == len(prices) or k == 0:
            return 0
        if holding == 0:
            return max(-prices[i] + dp(i + 1, k, 1), dp(i + 1, k, 0))
        if holding == 1:
            return max(prices[i] + dp(i + 1, k - 1, 0), dp(i + 1, k, 1))

    return dp(0, k, 0)


def maxProfitCooldown(prices: List[int]) -> int:
    @lru_cache(None)
    def dp(i, cooldown, holding):
        if i == len(prices):
            return 0
        if cooldown == 1:
            return dp(i + 1, 0, holding)
        if cooldown == 0 and holding == 0:
            return max(-prices[i] + dp(i + 1, 0, 1), dp(i + 1, 0, 0))
        if holding == 1:
            return max(prices[i] + dp(i + 1, 1, 0), dp(i + 1, 0, 1))

    return dp(0, 0, 0)


if __name__ == "__main__":
    print(maxProfitCooldown(prices=[1, 2, 3, 0, 2]))
    print(maxProfitCooldown(prices=[1]))
