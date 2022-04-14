from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for n in range(amount - coin + 1):
            dp[n + coin] += dp[n]
    return dp[amount]


if __name__ == "__main__":
    print(change(amount=5, coins=[1, 2, 5]))
    print(change(amount=3, coins=[2]))
    print(change(amount=10, coins=[10]))
