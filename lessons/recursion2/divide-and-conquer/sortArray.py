from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        i, j, ans = 0, 0, []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        if i < len(left):
            ans.extend(left[i:])
        if j < len(right):
            ans.extend(right[j:])
        return ans

    def mergeSort(arr):
        n = len(arr)
        if n <= 1:
            return arr
        pivot = n // 2
        left = mergeSort(arr[:pivot])
        right = mergeSort(arr[pivot:])
        return merge(left, right)

    return mergeSort(nums)


if __name__ == "__main__":
    print(sortArray(nums=[5, 2, 3, 1]))
    print(sortArray(nums=[5, 1, 1, 2, 0, 0]))
