from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    res, s_nums1, s_nums2 = [], sorted(nums1), sorted(nums2)
    i, j, n, m = 0, 0, len(s_nums1), len(s_nums2)

    while i < n and j < m:
        if s_nums1[i] == s_nums2[j]:
            res.append(s_nums1[i])
            i += 1
            j += 1
            continue
        
        if s_nums1[i] < s_nums2[j]:
            i += 1
            continue
        
        if s_nums1[i] > s_nums2[j]:
            j += 1
            continue

    return res


print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))
