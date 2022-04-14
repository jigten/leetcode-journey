from typing import List


# Introduction
def findMaxConsecutiveOnes(nums):
    cnt = 0
    ans = 0
    for num in nums:
        if num == 1:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    return ans


def sortedSquares(nums):
    n = len(nums)

    neg_end_idx = 0
    for idx, num in enumerate(nums):
        if num >= 0:
            neg_end_idx = idx
            break

    new_arr = []

    if neg_end_idx == 0 and nums[0] < 0:
        return map(lambda x: x * x, nums[::-1])

    i, j = neg_end_idx - 1, neg_end_idx
    while i >= 0 or j <= n:
        if i < 0 and j < n:
            new_arr += nums[j:]
            break

        if i >= 0 and j == n:
            if i == 0:
                new_arr.append(nums[0])
                break
            new_arr += nums[i::-1]
            break

        pos_num = nums[i] * -1

        if pos_num <= nums[j]:
            new_arr.append(pos_num)
            i -= 1
            continue

        if pos_num >= nums[j]:
            new_arr.append(nums[j])
            j += 1
            continue

    return map(lambda x: x * x, new_arr)


# Inserting items into an array
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    skipNext = False

    def shiftRightFromIndex(arr, index, n):
        for i in range(n - 1, index, -1):
            arr[i] = arr[i - 1]

    for i, num in enumerate(arr):
        if num != 0:
            continue

        if skipNext:
            skipNext = False
            continue

        if i + 1 < n:
            shiftRightFromIndex(arr, i + 1, n)
            arr[i + 1] = 0
            skipNext = True


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


# Deleting items from an array
def removeElement(nums: List[int], val: int) -> int:
    n = len(nums) - 1
    i = 0
    while i <= n:
        num = nums[i]
        if num == val and i == len(nums):
            del nums[i]
        if num == val:
            nums[i:] = nums[i + 1 :]
            i -= 1
            n -= 1
        i += 1


def removeDuplicates(nums: List[int]) -> int:
    n = len(nums) - 1
    i = 1
    while i <= n:
        if nums[i] == nums[i - 1] and i == len(nums):
            del nums[i]

        if nums[i] == nums[i - 1]:
            nums[i:] = nums[i + 1 :]
            i -= 1
            n -= 1
        i += 1


# Searching for items in an array
def checkIfExist(arr: List[int]) -> bool:
    complements = {}
    for i, num in enumerate(arr):
        complements[num / 2] = i

    for j, num in enumerate(arr):
        if num in complements and j != complements[num]:
            return True
    return False


def validMountainArray(arr: List[int]) -> bool:
    n = len(arr)

    if n < 3:
        return False

    if arr[0] > arr[1]:
        return False

    is_decreasing = False

    for i in range(1, n):
        if arr[i] > arr[i - 1] and not is_decreasing:
            continue

        if arr[i] < arr[i - 1] and not is_decreasing:
            is_decreasing = True
            continue

        if arr[i] < arr[i - 1] and is_decreasing:
            continue

        return False

    if not is_decreasing:
        return False

    return True


# In-place array operations
def replaceElements(arr: List[int]) -> List[int]:
    n = len(arr) - 1
    max_value = arr[n]
    arr[n] = -1

    for i in range(n - 1, -1, -1):
        temp_max = max_value
        if arr[i] > max_value:
            temp_max = arr[i]
        arr[i] = max_value
        max_value = temp_max
    return arr


def betterRemoveDuplicates(nums: List[int]) -> int:
    n = len(nums)
    w_p = 1
    for r_p in range(1, n):
        if nums[r_p] != nums[r_p - 1]:
            nums[w_p] = nums[r_p]
            w_p += 1
    return w_p


def moveZeroes(nums: List[int]) -> None:
    n = len(nums)
    w_p = 0
    zero_cnt = 0
    for r_p in range(n):
        if nums[r_p] != 0:
            nums[w_p] = nums[r_p]
            w_p += 1
        if nums[r_p] == 0:
            zero_cnt += 1
    nums[w_p:] = [0] * zero_cnt


def sortArrayByParity(nums: List[int]) -> List[int]:
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] % 2 > nums[j] % 2:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            continue
        if nums[i] % 2 == nums[j] % 2:
            if nums[i] % 2 == 0:
                i += 1
                continue
            if nums[j] % 2 != 0:
                j -= 1
                continue
        i += 1
        j -= 1
    return nums


def heightChecker(heights: List[int]) -> int:
    max_nr = max(heights)
    # initialize frequency array with 0's
    count = [0] * (max_nr + 1)
    # get frequencies
    for number in heights:
        count[number] += 1
    print(count)
    # create a sumcount array
    sumcount = [0] * (max_nr + 1)
    for index, number in enumerate(count[1:], start=1):
        sumcount[index] = number + sumcount[index - 1]
    # sumcount determines the index in sorted array
    # create output array
    print(sumcount)
    output = [0] * len(heights)
    # loop backwards starting with last element for stable sort
    for p in range(len(heights) - 1, -1, -1):
        output[sumcount[heights[p]] - 1] = heights[p]
        sumcount[heights[p]] -= 1
    print(output)
    # return the difference compared to original array
    result = 0
    for index, number in enumerate(heights):
        if number != output[index]:
            result += 1
    return result


def thirdMax(nums: List[int]) -> int:
    firstMax, secondMax, thirdMax = float("-inf"), float("-inf"), float("-inf")
    for num in nums:
        if num > firstMax:
            firstMax = num

    for num in nums:
        if num > secondMax and num < firstMax:
            secondMax = num

    for num in nums:
        if num > thirdMax and num < secondMax:
            thirdMax = num

    if thirdMax == float("-inf"):
        return firstMax

    return thirdMax


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    # o(n) space and time
    # counter = [0] * len(nums)
    # for num in nums:
    #     counter[num - 1] += 1
    # result = []
    # for i, num in enumerate(counter):
    #     if num == 0:
    #         result.append(i + 1)
    # return result

    # o(n) time and o(1) space
    for num in nums:
        nums[abs(num) - 1] = (
            -nums[abs(num) - 1] if nums[abs(num) - 1] > 0 else nums[abs(num) - 1]
        )

    res = [i + 1 for i, x in enumerate(nums) if x > 0]
    return res


if __name__ == "__main__":
    # nums1 = [1, 1, 2]
    # betterRemoveDuplicates(nums1)
    # print(nums1)

    # nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # betterRemoveDuplicates(nums2)
    # print(nums2)
    # print(replaceElements([400]))
    # nums = [1, 0, 3]
    # print(sortArrayByParity(nums))
    # print(thirdMax([1, 2]))
    print(findDisappearedNumbers([1, 1]))
