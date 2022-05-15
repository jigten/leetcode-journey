from bisect import bisect_left, bisect_right
from collections import Counter
from operator import itemgetter
from typing import List


def removeAnagrams(words: List[str]) -> List[str]:
    i, n = 0, len(words)
    words_copy = words.copy()
    while i < n - 1:
        if Counter(words_copy[i]) == Counter(words_copy[i+1]):
            words_copy.pop(i+1)
            n -= 1
            continue
        i += 1
    return words_copy

def maxConsecutive(bottom: int, top: int, special: List[int]) -> int:
    cons, curr_floor = [], bottom
    sorted_special = sorted(special)
    for i in range(len(sorted_special)):
        if sorted_special[i] > curr_floor:
            cons.append(sorted_special[i] - curr_floor)
            curr_floor = sorted_special[i] + 1
        else:
            curr_floor += 1
    
    if top > sorted_special[-1]:
        cons.append(top - sorted_special[-1])
    
    if len(cons) == 0:
        return 0
    return max(cons)

class CountIntervals:
    def __init__(self):
        self.intervals = []
        self.intervalCount = 0

    def add(self, left: int, right: int) -> None:
        if not self.intervals:
            self.intervals.append([left, right])
            self.intervalCount = right - left + 1
            return

        l = bisect_left(self.intervals, left, key=itemgetter(1))
        r = bisect_right(self.intervals, right, key=itemgetter(0))
        
        if l < len(self.intervals):
            left = min(left, self.intervals[l][0])
            
        if r > 0:
            right = max(right, self.intervals[r-1][1])
        
        to_add = right - left + 1
        
        to_remove = 0
        for i in range(l, r):
            to_remove += self.intervals[i][1] - self.intervals[i][0] + 1
            
        self.intervalCount += to_add - to_remove
        self.intervals[l:r] = [[left, right]]


    def count(self) -> int:
        return self.intervalCount

# print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))
# print(removeAnagrams(["a","b","c","d","e"]))

# print(maxConsecutive(bottom = 2, top = 9, special = [4,6]))
# print(maxConsecutive(bottom = 6, top = 8, special = [7,6,8]))
# print(maxConsecutive(3, 15, [7,9,13]))

