from collections import defaultdict
from itertools import permutations
from typing import List


def findKDistantIndices(nums: List[int], key: int, k: int) -> List[int]:
    js = []
    for i, num in enumerate(nums):
        if num == key:
            js.append(i)
    min_j, max_j = min(js), max(js)

    s = min_j - k if min_j - k >= 0 else 0
    e = max_j + k if max_j + k < len(nums) else len(nums) - 1
    return [x for x in range(s, e + 1)]


def digArtifacts(n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
    count = 0
    for artifact in artifacts:
        if artifact[0:2] == artifact[2:4] and artifact[0:2] in dig:
            count += 1
            continue

        if artifact[0:2] in dig and (
            artifact[2:4] in dig
            or any([x > artifact[2] and y > artifact[3] for [x, y] in dig])
        ):
            count += 1
            continue
    return count


def maximumTop(nums: List[int], k: int) -> int:
    n = len(nums)
    if n == 1:
        if k % 2 == 1:
            return -1
        else:
            return nums[0]
    elif k > n:
        return max(nums)
    elif k == n:
        if max(nums) == nums[-1]:
            return sorted(nums)[-2]
        else:
            return max(nums)
    elif k == 0:
        return nums[0]
    elif k == 1:
        return nums[1]
    else:
        max_popped = max(nums[0 : k - 1])
        return max_popped if max_popped > nums[k] else nums[k]


if __name__ == "__main__":
    print(
        digArtifacts(n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1]])
    )
    print(
        digArtifacts(
            n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1], [1, 1]]
        )
    )
