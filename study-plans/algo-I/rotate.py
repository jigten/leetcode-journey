from typing import List


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    adjusted_k = k % n
    nums[:] = nums[n-adjusted_k:] + nums[:n-adjusted_k]
        
nums1 = [1,2,3,4,5,6,7]
rotate(nums1, 3)
print(nums1)

nums2 = [-1,-100,3,99]
rotate(nums2, 2)
print(nums2)

nums3 = [1,2,3]
rotate(nums3, 2)
print(nums3)


