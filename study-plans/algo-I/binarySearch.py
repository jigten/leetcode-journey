from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    
    while l < r:
        mid = l + (r - l) // 2
        curr = nums[mid]

        if curr == target:
            return mid

        if curr < target:
            l = mid + 1
        
        if curr > target:
            r = mid

    return -1

print(search([-1,0,3,5,9,12], 9))
print(search( [-1,0,3,5,9,12], 2))
