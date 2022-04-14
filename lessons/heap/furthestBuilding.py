import heapq
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    heap = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(heap, diff)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
        if bricks < 0:
            return i
    return len(heights) - 1


if __name__ == "__main__":
    print(furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
    print(
        furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2)
    )
    print(furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))
