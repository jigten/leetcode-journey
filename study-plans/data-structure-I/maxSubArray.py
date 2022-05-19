from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum, local_max = float('-inf'), 0
    for num in nums:
        local_max = max(num, local_max + num)
        if local_max > max_sum:
            max_sum = local_max

    return max_sum
