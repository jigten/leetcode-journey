from itertools import accumulate
from typing import List


def percentageLetter(s: str, letter: str) -> int:
        count, n = s.count(letter), len(s)
        return (count * 100) // n

# print(percentageLetter("foobar", "o"))
# print(percentageLetter("jjjj", "k"))

def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    count, pairs = 0, list(zip(capacity, rocks))
    s_pairs = sorted(pairs, key=lambda x: x[0] - x[1])

    for c, r in s_pairs:
        if c == r:
            count += 1
            continue
        
        if c > r and additionalRocks + r >= c:
            additionalRocks -= c - r
            count += 1

    return count

# print(maximumBags([2,3,4,5], [1,2,4,4], 2))
# print(maximumBags([10,2,2], [2,2,0], 100))
# print(maximumBags([54,18,91,49,51,45,58,54,47,91,90,20,85,20,90,49,10,84,59,29,40,9,100,1,64,71,30,46,91], [14,13,16,44,8,20,51,15,46,76,51,20,77,13,14,35,6,34,34,13,3,8,1,1,61,5,2,15,18], 77))


def minimumLines(stockPrices: List[List[int]]) -> int:
    s_stocks = sorted(stockPrices, key=lambda x: x[0])
    count = len(s_stocks) - 1
    for i in range(1, len(stockPrices) - 1):
        a, b, c = s_stocks[i - 1], s_stocks[i], s_stocks[i + 1]
        if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
            count -= 1
    return count

# print(minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
# print(minimumLines([[3,4],[1,2],[7,8],[2,3]]))
# print(minimumLines([[36,9],[17,93],[34,4],[30,11],[11,41],[53,36],[5,92],[81,92],[28,36],[3,45],[72,33],[64,1],[4,70],[16,73],[99,20],[49,33],[47,74],[83,91]]))
# print(minimumLines([[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]]))
# print(minimumLines([[1,1]]))
# print(minimumLines([[1,1] ,[2,1]]))

def totalStrength(A):
    mod = 10 ** 9 + 7
    n = len(A)
    
    # next small on the right
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and A[stack[-1]] > A[i]:
            right[stack.pop()] = i
        stack.append(i)

    # next small on the left
    left = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            left[stack.pop()] = i
        stack.append(i)

    # for each A[i] as minimum, calculate sum
    res = 0
    acc = list(accumulate(accumulate(A), initial = 0))
    print(acc)
    for i in range(n):
        l, r = left[i], right[i]
        lacc = acc[i] - acc[max(l, 0)]
        racc = acc[r] - acc[i]
        ln, rn = i - l, r - i
        res += A[i] * (racc * ln - lacc * rn)
    return res

print(totalStrength([1, 3, 1, 2]))
