from typing import List


def countPrefixes(words: List[str], s: str) -> int:
    count = 0
    for word in words:
        if word == s or s.startswith(word):
            count += 1

    return count

def minimumAverageDifference(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    prev_sum = sum(nums[:1])
    next_sum = sum(nums[1:])
    p_len = 1
    n_len = n - 1
    minimum = abs(prev_sum // p_len - next_sum // n_len)
    min_i = 0
    for i in range(1, n):
        prev_sum += nums[i]
        p_len += 1
        next_sum -= nums[i]
        n_len -= 1
        if n_len != 0:
            candiate_min = abs(prev_sum // p_len - next_sum // n_len)
        else:
            candiate_min = abs(prev_sum // p_len)

        if candiate_min < minimum:
            minimum = candiate_min
            min_i = i

    return min_i

def countUnguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    unguarded =  m * n
    
    for wall in walls:
        r, c = wall
        print(r, c)
        for i in range(0, c):
            if [i, c] in guards:
                print('guard at (%d, %d)' % (r, i))
                unguarded -= c - i
                break

        for i in range(c + 1, m):
            if [i, c] in guards:
                print('guard at (%d, %d)' % (r, i))
                unguarded -= i - c
                break
        
        for i in range(0, r):
            if [i, c] in guards:
                print('guard at (%d, %d)' % (r, i))
                unguarded -= r - i
                break
        
        for i in range(r + 1, n):
            if [i, c] in guards:
                print('guard at (%d, %d)' % (r, i))
                unguarded -= i - r
                break
    return unguarded - len(walls) - len(guards)

print(countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))
print(countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]))
