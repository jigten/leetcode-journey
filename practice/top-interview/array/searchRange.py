from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    l, r, li = 0, len(nums) - 1, -1

    while l <= r:
        mid = l + (r - l) // 2
        val = nums[mid]
        if val == target:
            li = mid
            r = mid-1
        elif val > target:
            r = mid-1
        else:
            l = mid + 1

    l, r, ri = 0, len(nums) - 1, -1
    while l <= r:
        mid = l + (r - l) // 2
        val = nums[mid]
        if val == target:
            ri = mid
            l = mid + 1
        elif val > target:
            r = mid-1
        else:
            l = mid + 1
    
    return [li, ri]


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([], 0))
print(searchRange([1], 1))
