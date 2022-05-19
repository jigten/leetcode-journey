from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) < 1:
        return 0
    min_price = prices[0]
    max_profit = 0        
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
