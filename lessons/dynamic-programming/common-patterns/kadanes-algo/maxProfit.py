from typing import List


def maxProfit(prices: List[int]) -> int:
    current, best = 0, 0
    for i in range(1, len(prices)):
        current = max(current + prices[i] - prices[i - 1], prices[i] - prices[i - 1])
        best = max(best, current)
        print(i, current, best)
    return best


if __name__ == "__main__":
    print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(maxProfit(prices=[7, 6, 4, 3, 1]))
