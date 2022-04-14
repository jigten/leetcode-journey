from typing import List


def maxSubArray(nums: List[int]) -> int:
    current, best = 0, float("-inf")
    for num in nums:
        current = max(current + num, num)
        best = max(best, current)
    return best


if __name__ == "__main__":
    print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray(nums=[1]))
    print(maxSubArray(nums=[5, 4, -1, 7, 8]))
