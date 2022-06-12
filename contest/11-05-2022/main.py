from collections import defaultdict
from typing import List


def strongPasswordCheckerII(password: str) -> bool:
    specials = "!@#$%^&*()-+"
    if len(password) < 8:
        return False
    
    hasLower, hasUpper, hasSpecial, hasDigit = False, False, False, False
    prev = ''
    
    for i in range(len(password)):
        c = password[i]
        if prev and c == prev:
            return False
        prev = c
        if c in specials:
            hasSpecial = True
        if c.isupper():
            hasUpper = True
        if c.islower():
            hasLower = True
        if c.isdigit():
            hasDigit = True
            
    return hasLower and hasUpper and hasSpecial and hasDigit

# print(strongPasswordCheckerII("yvTY#@IB#*!hjrQt-TLW&z)$@!%Duqt&ToskxHgnybqpndMI+wP&fcemIk#@KnkMTaUkcIbncpTL"))

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    spells = sorted(enumerate(spells), key=lambda i: i[1])
    potions.sort()
    output = [0] * len(spells)

    for orgIdx, s in spells:
        l, r = 0, len(potions) - 1
        while l < r:
            mid = l + (r - l) // 2
            power = potions[mid] * s
            if power < success:
                l = mid + 1
            else:
                r = mid

        if l == len(potions) - 1:
            if potions[l] * s >= success:
                output[orgIdx] = 1
            else:
                output[orgIdx] = 0
        else:    
            output[orgIdx] = len(potions) - l
    return output

# print(successfulPairs([5,1,3], [1,2,3,4,5], 7))
# print(successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16))
# print(successfulPairs([1,2,3,4,5,6,7], [1,2,3,4,5,6,7], 25))
# print(successfulPairs([20,26,38,23,23,20,14,30], [24,1,7,26,19,17,7], 510))
# print(successfulPairs([40,11,24,28,40,22,26,38,28,10,31,16,10,37,13,21,9,22,21,18,34,2,40,40,6,16,9,14,14,15,37,15,32,4,27,20,24,12,26,39,32,39,20,19,22,33,2,22,9,18,12,5], [31,40,29,19,27,16,25,8,33,25,36,21,7,27,40,24,18,26,32,25,22,21,38,22,37,34,15,36,21,22,37,14,31,20,36,27,28,32,21,26,33,37,27,39,19,36,20,23,25,39,40], 600))

def matchReplacement(s: str, sub: str, mappings: List[List[str]]) -> bool:
    mappingsMap = defaultdict(list)
    for c, r in mappings:
        mappingsMap[c].append(r)

    def dfs(s, sub):
        if sub in s:
            return True
        for i, c in enumerate(sub):
            if c in mappingsMap:
                for r in mappingsMap[c]:
                    if dfs(s, sub[:i] + r + sub[i+1:]):
                        return True

        return False
    
    return dfs(s, sub)

print(matchReplacement(s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]))
print(matchReplacement(s = "fooleetbar", sub = "f00l", mappings = [["o","0"]]))
print(matchReplacement(s = "Fool33tbaR", sub = "leetd", mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]))


# def countSubarrays(nums: List[int], k: int) -> int:
#     def findSubarraySum(arr, n, Sum):
#         prevSum = defaultdict(lambda : 0)
#         res = 0
#         currsum = 0
#         for i in range(0, n): 
#             currsum += arr[i]
#             if currsum < Sum: 
#                 res += 1        
#             if (currsum - Sum) in prevSum:
#                 res += prevSum[currsum - Sum]
#             prevSum[currsum] += 1
#         return res
#     return findSubarraySum(nums, len(nums), k)

# print(countSubarrays(nums = [2,1,4,3,5], k = 10))
