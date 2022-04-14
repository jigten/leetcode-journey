import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    maxHeap = [-x for x in nums]
    heapq.heapify(maxHeap)
    res = 0
    for _ in range(k):
        res = heapq.heappop(maxHeap)
    return res * -1


if __name__ == "__main__":
    print(findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
