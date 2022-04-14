from functools import lru_cache
from typing import List


def maxProfit(prices: List[int], fee: int) -> int:
    @lru_cache(None)
    def dp(i, holding):
        if i == len(prices):
            return 0

        maxProfit = 0
        if holding == 0:
            maxProfit = max(-prices[i] + dp(i + 1, 1), dp(i + 1, 0))
        if holding == 1:
            maxProfit = max(prices[i] + dp(i + 1, 0) - fee, dp(i + 1, 1))

        return maxProfit

    return dp(0, 0)


if __name__ == "__main__":
    print(maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
    print(maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
