from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    two_back, one_back = cost[0], cost[1]
    for i in range(2, len(cost)):
        temp = cost[i] + min(one_back, two_back)
        one_back, two_back = temp, one_back
    return min(two_back, one_back)


if __name__ == "__main__":
    print(minCostClimbingStairs(cost=[10, 15, 20]))
    print(minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
