import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    if len(stones) == 1:
        return stones[0]

    maxHeap = [-x for x in stones]
    heapq.heapify(maxHeap)

    while maxHeap:
        if len(maxHeap) == 1:
            return -maxHeap[0]

        x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
        if x == y:
            continue
        else:
            heapq.heappush(maxHeap, -(x - y))

    return 0


if __name__ == "__main__":
    print(lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
    print(lastStoneWeight(stones=[1]))
    print(lastStoneWeight(stones=[3, 7, 2]))
