import math
from collections import Counter
from typing import List, Optional


def countEven(num: int) -> int:
    res = 0
    for i in range(1, num + 1):
        digitSum = sum([int(x) for x in str(i)])
        if digitSum % 2 == 0:
            res += 1
    return res


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    ans = ListNode(0)
    ans_head = ans
    s_p, e_p = head, head
    curr_sum = 0
    while e_p and e_p.next:
        if s_p.val == 0:
            e_p = e_p.next
            while e_p.val != 0:
                curr_sum += e_p.val
                e_p = e_p.next
            ans.next = ListNode(curr_sum)
            ans = ans.next
            curr_sum = 0
            s_p = e_p

    return ans_head.next


def repeatLimitedString(s: str, repeatLimit: int) -> str:
    def nextChar(charset, start):
        for i in range(start - 1, -1, -1):
            if charset[i] > 0:
                charset[i] -= 1
                return chr(i + ord("a"))
        return None

    repeatLimitedString = ""
    chars = [0] * (26)
    for i in s:
        chars[ord(i) - ord("a")] += 1

    for i in range(25, -1, -1):
        count = 0
        while chars[i] > 0:
            repeatLimitedString += chr(i + ord("a"))
            chars[i] -= 1
            count += 1
            if chars[i] > 0 and count == repeatLimit:
                next_char = nextChar(chars, i)
                if not next_char:
                    return repeatLimitedString
                repeatLimitedString += next_char
                count = 0

    return repeatLimitedString


"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.
"""


def coutPairs(nums: List[int], k: int) -> int:
    N, output = len(nums), 0
    divisors = []
    counter = Counter()

    for i in range(1, k + 1):
        if k % i == 0:
            divisors.append(i)
    print("divisors", divisors)
    for i in range(0, N):
        remainder = k // math.gcd(k, nums[i])
        print("remainder", remainder)
        output += counter[remainder]
        for divisor in divisors:
            if nums[i] % divisor == 0:
                counter[divisor] += 1
    print("counter", counter)
    return output


if __name__ == "__main__":
    print(coutPairs(nums=[1, 2, 3, 4, 5], k=2))
    # print(coutPairs(nums=[1, 2, 3, 4], k=5))
    # print(coutPairs([3, 2, 6, 1, 8, 4, 1], 3))
    # print(coutPairs([8, 10, 2, 5, 9, 6, 3, 8, 2], 6))
