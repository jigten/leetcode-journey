from typing import List


def sortColors(nums: List[int]) -> None:
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

nums1 = [2,0,2,1,1,0]
sortColors(nums1)
print(nums1)

nums2 = [2,0,1]
sortColors(nums2)
print(nums2)
