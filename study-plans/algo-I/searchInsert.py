from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while (l < r):
        mid = l + (r - l) // 2
        curr = nums[mid]
        
        if curr == target:
            return mid
        
        if curr < target:
            l = mid + 1

        else:
            r = mid

    return l

print(searchInsert([1,3,5,6], 2))
