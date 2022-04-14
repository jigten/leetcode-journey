from typing import List


def pivotIndex(nums: List[int]) -> int:
    i, ls, rs = 0, 0, sum(nums[1:])
    if ls == rs:
        return i

    while i < len(nums) - 1:
        i += 1
        ls += nums[i - 1]
        rs -= nums[i]
        if ls == rs:
            return i

    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
print(pivotIndex([2, 1, -1]))
print(pivotIndex([-1, -1, 0, 1, 1, 0]))
