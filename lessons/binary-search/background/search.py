from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    mid = (right + left) // 2
    while nums[mid] != target:
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
        newMid = (right + left) // 2
        if newMid == mid or newMid >= len(nums):
            return -1
        mid = newMid
    return mid


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))
    print(search([-1, 0, 3, 5, 9, 12], 2))
    print(search([-1, 0, 3, 5, 9, 12], 13))
