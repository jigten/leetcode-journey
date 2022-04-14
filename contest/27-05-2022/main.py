from collections import Counter
from functools import lru_cache
from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    ans_1, ans_2 = [], []
    for x in nums1:
        if x not in nums2:
            ans_1.append(x)

    for y in nums2:
        if y not in nums1:
            ans_2.append(y)

    return [list(set(ans_1)), list(set(ans_2))]


def minDeletion(nums: List[int]) -> int:
    n, count, flag = len(nums), 0, True
    for i in range(n):
        if flag:
            if i % 2 == 0 and i != n - 1 and nums[i] == nums[i + 1]:
                count += 1
                flag = False
        else:
            if i % 2 == 1 and i != n - 1 and nums[i] == nums[i + 1]:
                count += 1
                flag = True

    currLength = n - count
    return count if currLength % 2 == 0 else count + 1


def kthPalindrome(queries: List[int], intLength: int) -> List[int]:
    return


def maxValueOfCoins(piles: List[List[int]], k: int) -> int:
    N = len(piles)

    @lru_cache(None)
    def dp(n, k):
        if n == N:
            if k == 0:
                return 0
            if k > 0:
                return float("-inf")
        ans = dp(n + 1, k)
        sm = 0
        for i in range(min(k, len(piles[n]))):
            sm += piles[n][i]
            ans = max(ans, dp(n + 1, k - i - 1) + sm)
        return ans

    return dp(0, k)


print(maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))
print(
    maxValueOfCoins(
        piles=[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], k=7
    )
)
