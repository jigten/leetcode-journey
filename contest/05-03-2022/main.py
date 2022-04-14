from collections import defaultdict
from typing import List


def mostFrequent(nums: List[int], key: int) -> int:
    counts = defaultdict(int)
    for i, num in enumerate(nums):
        if num == key and i + 1 < len(nums):
            counts[nums[i + 1]] += 1
    return max(counts, key=counts.get)


def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
    mapped_vals = []
    for num in nums:
        res = ""
        for c in str(num):
            res += str(mapping[int(c)])
        mapped_vals.append(int(res))
    order = sorted(list(range(len(mapped_vals))), key=lambda i: mapped_vals[i])
    return [nums[i] for i in order]


def minMovesToMakePalindrome(s: str) -> int:
    s, n = list(s), len(s)
    odd_len = False
    if n % 2 != 0:
        odd_len = True
    odd_occur = 0
    odd_val = 0
    count = 0
    ans = True
    i = 0
    while i < (n // 2):
        l = i
        r = n - l - 1
        while l < r:
            if s[l] == s[r]:
                break
            else:
                r -= 1
        if l == r:
            if odd_len:
                if odd_occur == 0 or odd_val == s[l]:
                    odd_val = s[l]
                    odd_occur += 1
                    s[l], s[l + 1] = s[l + 1], s[l]
                    count += 1
                continue
            ans = False
            break
        else:
            for j in range(r, n - l - 1):
                (s[j], s[j + 1]) = (s[j + 1], s[j])
                count += 1
        i += 1

    if ans:
        return count
    else:
        return -1


if __name__ == "__main__":
    # print(minMovesToMakePalindrome("letelt"))
    # print(minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii"))

    print(
        sortJumbled(
            [8, 2, 9, 5, 3, 7, 1, 0, 6, 4],
            [
                418,
                4191,
                916,
                948,
                629641556,
                574,
                111171937,
                28250,
                42775632,
                6086,
                85796326,
                696292542,
                186,
                67559,
                2167,
                366,
                854,
                2441,
                78176,
                621,
                4257,
                2250097,
                509847,
                7506,
                77,
                50,
                4135258,
                4036,
                59934,
                59474,
                3646243,
                9049356,
                85852,
                90298188,
                2448206,
                30401413,
                33190382,
                968234660,
                7973,
                668786,
                992777977,
                77,
                355766,
                221,
                246409664,
                216290476,
                45,
                87,
                836414,
                40952,
            ],
        )
    )
