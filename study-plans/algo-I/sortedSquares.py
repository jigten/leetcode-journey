from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    answer = [0] * len(nums)
    l, r = 0, len(nums) - 1
    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))
print(sortedSquares([-5,-3,-2,-1]))
