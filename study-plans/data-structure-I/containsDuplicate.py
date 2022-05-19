
from collections import defaultdict
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    occurences = defaultdict(bool)
    for num in nums:
        if occurences[num]:
            return True
        occurences[num] = True
