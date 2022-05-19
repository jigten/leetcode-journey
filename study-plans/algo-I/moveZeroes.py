from typing import List


def moveZeroes(nums: List[int]) -> None:
    s, n = 0, len(nums)
    if n == 1:
        return
    
    for f in range(n):
        if nums[f] != 0 and nums[s] == 0:
            nums[s], nums[f] = nums[f], nums[s]
        if nums[s] != 0:
            s += 1
    


nums1 = [0,1,0,3,12]
moveZeroes(nums1)
print(nums1)

nums2 = [0]
moveZeroes(nums2)
print(nums2)
