from bisect import bisect_right
from typing import List


def divisorSubstrings(num: int, k: int) -> int:
    count = 0
    num_str = str(num)
    s_i, e_i = 0, k
    while e_i <= len(num_str):
        curr = int(num_str[s_i:e_i])
        if curr == 0:
            s_i += 1
            e_i += 1
            continue

        if num % curr == 0:
            count += 1
        s_i += 1
        e_i += 1
    return count

def waysToSplitArray(nums: List[int]) -> int:
    res, n = 0, len(nums)
    ls, rs = nums[0], sum(nums[1:]) 
    for i in range(1, n):
        if ls >= rs:
            res += 1
        ls += nums[i]
        rs -= nums[i]
    return res

def maximumWhiteTiles(tiles: List[List[int]], carpetLen: int) -> int:
    # sort the tiles by the starting position
    tiles.sort(key = lambda x:x[0])
    # build the starting position array
    startPos = [tiles[i][0] for i in range(len(tiles))]
    # build the prefix sum array
    preSum = [0] * (len(tiles) + 1)
    for i in range(1, len(tiles) + 1):
        preSum[i] = preSum[i - 1] + (tiles[i-1][1]-tiles[i-1][0] + 1)

    res = 0
    for i in range(len(tiles)):
        s, e = tiles[i]
        # if the length of tile >= length of carpet, return carpetLen
        if e >= s + carpetLen - 1:
            return carpetLen
        # binary search the index of the ending tile that the carpet can partially cover
        endIdx = bisect_right(startPos, s + carpetLen - 1) - 1
        # calculate the length of the ending tile that the carpet cannot cover 
        compensate = 0
        if tiles[endIdx][1] > s + carpetLen - 1:
            compensate = tiles[endIdx][1] - s - carpetLen + 1
        # update the result
        res = max(res, preSum[endIdx+1] - preSum[i] - compensate)
        
    return res

# print(divisorSubstrings(num = 240, k = 2))
# print(divisorSubstrings(num = 430043, k = 2))

# print(waysToSplitArray([10,4,-8,7]))
# print(waysToSplitArray([2,3,1,0]))

print(maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))
print(maximumWhiteTiles(tiles = [[10,11],[1,1]], carpetLen = 2))
print(maximumWhiteTiles([[1,1000000000]], 1000000000))
print(maximumWhiteTiles([[1,1]], 1))
