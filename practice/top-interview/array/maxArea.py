from typing import List


def maxArea(height: List[int]) -> int:
    i, j = 0, len(height) - 1
    water = 0
    while i < j:
        water = max(water, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return water

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
