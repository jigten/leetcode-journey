from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    out = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(i[1], out[-1][1])
        else:
            out.append(i)
    return out

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
