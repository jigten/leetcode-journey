from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    n = len(costs) // 2
    totalCost = sum([x[0] for x in costs])
    refundCosts = [x[1] - x[0] for x in costs]
    refundCosts.sort()
    for i in range(n):
        totalCost += refundCosts[i]
    return totalCost


print(twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
print(
    twoCitySchedCost(
        [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    )
)
print(
    twoCitySchedCost(
        costs=[
            [515, 563],
            [451, 713],
            [537, 709],
            [343, 819],
            [855, 779],
            [457, 60],
            [650, 359],
            [631, 42],
        ]
    )
)
