from collections import defaultdict
from functools import lru_cache
from typing import List


def convertTime(current: str, correct: str) -> int:
    res = 0
    current = list(map(int, current.split(":")))
    correct = list(map(int, correct.split(":")))
    current_Hours, correct_Hours = current[0], correct[0]
    current_Minutes, correct_Minutes = current[1], correct[1]
    if current_Hours <= correct_Hours and current_Minutes <= correct_Minutes:
        res += correct_Hours - current_Hours
        minutes_diff = correct_Minutes - current_Minutes
        while minutes_diff != 0:
            if minutes_diff >= 15:
                minutes_diff -= 15
                res += 1
                continue
            elif minutes_diff >= 5:
                minutes_diff -= 5
                res += 1
                continue
            else:
                minutes_diff -= 1
                res += 1
                continue

    elif current_Hours < correct_Hours and current_Minutes > correct_Minutes:
        res += correct_Hours - current_Hours - 1
        minutes_diff = (60 - current_Minutes) + correct_Minutes
        while minutes_diff != 0:
            if minutes_diff >= 15:
                minutes_diff -= 15
                res += 1
                continue
            elif minutes_diff >= 5:
                minutes_diff -= 5
                res += 1
                continue
            else:
                minutes_diff -= 1
                res += 1
                continue
    return res


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    winners = set()
    losers = set()
    one_time_losers = defaultdict(int)

    for match in matches:
        winners.add(match[0])
        losers.add(match[1])
        one_time_losers[match[1]] += 1

    never_lost = winners.difference(losers)
    return [
        sorted(list(never_lost)),
        sorted([k for k, v in one_time_losers.items() if v == 1]),
    ]


def maximumCandies(candies: List[int], k: int) -> int:
    l, r = 1, max(candies)
    while l < r:
        mid = (l + r) // 2
        if sum(candy // mid for candy in candies) >= k:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(maximumCandies(candies=[5, 8, 6], k=3))
print(maximumCandies(candies=[2, 5], k=11))
print(maximumCandies([4, 7, 5], 4))
