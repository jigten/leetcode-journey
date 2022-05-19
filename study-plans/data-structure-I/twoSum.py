from collections import defaultdict
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    complements = defaultdict(int)
    for i, num in enumerate(nums):
        complements[target - num] = i
    
    for i, num in enumerate(nums):
        if num in complements and i != complements[num]:
            return [i, complements[num]]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
