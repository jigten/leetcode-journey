from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:
    arr_sum, current_max, best_max, current_min, best_min = (
        0,
        0,
        nums[0],
        0,
        nums[0],
    )
    for num in nums:
        current_max = max(current_max + num, num)
        best_max = max(best_max, current_max)
        current_min = min(current_min + num, num)
        best_min = min(best_min, current_min)
        arr_sum += num
    return max(best_max, arr_sum - best_min) if best_max > 0 else best_max


if __name__ == "__main__":
    print(maxSubarraySumCircular(nums=[1, -2, 3, -2]))
    print(maxSubarraySumCircular(nums=[5, -3, 5]))
    print(maxSubarraySumCircular(nums=[-3, -2, -3]))
