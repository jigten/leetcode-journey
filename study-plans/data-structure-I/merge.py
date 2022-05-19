from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if n == 0:
        return

    if m == 0:
        nums1[:] = nums2

    i, j, adj_m = 0, 0, m

    while i < adj_m and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
            continue
        nums1[:] = nums1[:i] + [nums2[j]] + nums1[i:]
        i += 1
        adj_m += 1
        j += 1
        
    if j < n:
        nums1[:] = nums1[:i] + nums2[j:]
    else:
        nums1[:] = nums1[: m + n]
    
n1 = [1,2,3,0,0,0]
merge(n1, 3, [2,5,6], 3)
print(n1)

n2 = [1]
merge(n2, 1, [], 0)
print(n2)

n3 = [0]
merge(n3, 0, [1], 1)
print(n3)

n4 = [1,5,6,0,0,0]
merge(n4, 3, [2,3,4], 3)
print(n4)
