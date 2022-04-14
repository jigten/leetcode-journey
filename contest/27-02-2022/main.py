from collections import Counter
from typing import List


def prefixCount(words: List[str], pref: str) -> int:
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count


def minSteps(s: str, t: str) -> int:
    s_counter = Counter(s)
    t_counter = Counter(t)

    steps = 0
    for key, value in s_counter.items():
        if key in t_counter:
            steps += abs(value - t_counter[key])
        else:
            steps += value
    for key, value in t_counter.items():
        if key in s_counter:
            steps += abs(value - t_counter[key])
        else:
            steps += value
    return steps


def minimumTime(time: List[int], totalTrips: int) -> int:
    lo, hi = 1, max(time) * totalTrips

    def f(x):
        return sum(x // t for t in time) >= totalTrips

    while lo < hi:
        mid = (lo + hi) // 2
        if not f(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    print(minimumTime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
