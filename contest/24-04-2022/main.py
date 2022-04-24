from bisect import bisect_left
from collections import defaultdict
from operator import itemgetter
from typing import List


def intersection(nums):
    res = set.intersection(*map(set, nums))
    return sorted(list(res))

def countLatticePoints(circles):
    points = []
    for circle in circles:
        x, y, r = circle
        if r <= 0:
            continue        
        for x0 in range(x - r, x + r + 1):
            for y0 in range(y - r, y + r + 1):
                if (x0 - x) ** 2 + (y0 - y) ** 2 <= r ** 2:
                    points.append((x0, y0))
    return len(set(points))

def countRectangles(rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
    sorted_rects = sorted(rectangles, key=itemgetter(0))
    rects = defaultdict(list)
    res = []
    for l, h in sorted_rects:
        rects[h].append(l)
    
    for x, y in points:
        r = 0
        for h in rects:
            if h >= y:
                r += len(rects[h]) - bisect_left(rects[h], x)
        res.append(r)
    return res

print(countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]]))
print(countRectangles([[1,1],[2,2],[3,3]], [[1,3],[1,1]]))
