import string
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from itertools import permutations
from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def maxDepth(root):
#     if not root:
#         return 0

#     return max(maxDepth(root.left), maxDepth(root.right)) + 1


# def isValidBST(root):
#     def helper(node, lower, higher):
#         if not node:
#             return True

#         if lower < node.val < higher:
#             return helper(node.left, lower, node.val) and helper(
#                 node.right, node.val, higher
#             )

#         return False

#     return helper(root, float("-inf"), float("inf"))


def isSymmetric(root):
    def helper(node, left, right):
        if not node:
            return True

        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val == right.val:
            return helper(left, left.left, right.right) and helper(
                right, left.right, right.left
            )
        else:
            return False

    return helper(root, root.left, root.right)


def countValidWords(sentence):
    count = 0

    def isValidWord(word):
        if word == "":
            return False

        hyphen_count = 0
        punctuation_count = 0

        for idx, char in enumerate(word):
            if (idx == 0 or idx == len(word) - 1) and char == "-":
                return False

            if char in ["!", ".", ","] and idx != len(word) - 1:
                return False

            if char == "-":
                hyphen_count += 1
                if word[idx - 1].isdigit() or word[idx - 1] in ["!", ".", ","]:
                    return False
                if word[idx + 1].isdigit() or word[idx + 1] in ["!", ".", ","]:
                    return False
                if hyphen_count > 1:
                    return False

            if char in ["!", ".", ","]:
                punctuation_count += 1
                if punctuation_count > 1:
                    return False

            if char.isdigit():
                return False
        return True

    tokens = sentence.split(" ")

    for word in tokens:
        if isValidWord(word):
            print(word)
            count += 1

    return count


def nextBeautifulNumber(n):
    def countOccurrances(num, d):
        count = 0

        # Loop to find the digits of N
        while num > 0:

            # check if the digit is D
            if num % 10 == d:
                count = count + 1

            num = num // 10

        # return the count of the
        # occurrences of D in N
        return count

    def checkIfBeautiful(number):
        unique_nums = set(str(number))
        for num in unique_nums:
            if countOccurrances(number, int(num)) != int(num):
                return False
        return True

    temp = n + 1
    while checkIfBeautiful(temp) == False:
        temp += 1
    return temp


def countHighestScoreNodes(parents):
    max_score = 0
    count = 0

    for i in range(0, len(parents)):
        return

    return


def smallestEqual(nums):
    for i, num in enumerate(nums):
        if i % 10 == num:
            return i
    return -1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodesBetweenCriticalPoints(head):
    critical_points_indices = []
    prev_node = head
    next_node = head.next.next
    curr_index = 2

    while next_node != None:
        if prev_node.val > prev_node.next.val < next_node.val:
            critical_points_indices.append(curr_index)

        if prev_node.val < prev_node.next.val > next_node.val:
            critical_points_indices.append(curr_index)

        prev_node = prev_node.next
        next_node = next_node.next
        curr_index += 1

    if not critical_points_indices or len(critical_points_indices) == 1:
        return [-1, -1]

    min_dist = 10 ** 10
    for i in range(len(critical_points_indices) - 1):
        if critical_points_indices[i + 1] - critical_points_indices[i] < min_dist:
            min_dist = critical_points_indices[i + 1] - critical_points_indices[i]

    max_dist = (
        critical_points_indices[len(critical_points_indices) - 1]
        - critical_points_indices[0]
    )
    return [min_dist, max_dist]


def minimumOperations(nums, start, goal):
    x = start
    num_transformations = 1
    next_transformed_vals = []

    for num in nums:
        next_transformed_vals.append(x + num)
        next_transformed_vals.append(x - num)
        next_transformed_vals.append(x ^ num)

    while any(0 <= x <= 1000 for x in next_transformed_vals):
        temp_arr = []

        if goal in next_transformed_vals:
            return num_transformations
        for transformed in next_transformed_vals:
            for num in nums:
                temp_arr.append(transformed + num)
                temp_arr.append(transformed - num)
                temp_arr.append(transformed ^ num)

        if all(elem in temp_arr for elem in next_transformed_vals):
            return -1

        next_transformed_vals = temp_arr
        num_transformations += 1

    if goal in next_transformed_vals:
        return num_transformations

    return -1


def timeRequiredToBuy(tickets, k):
    time_taken = 0
    tickets_left = tickets[k]

    while tickets_left > 0:
        for i, t in enumerate(tickets):
            if t != 0 and i != k:
                tickets[i] = tickets[i] - 1
                time_taken += 1

            if t == 0 and i != k:
                continue

            if t != 0 and i == k:
                tickets[i] = tickets[i] - 1
                tickets_left = tickets[i]
                time_taken += 1

                if tickets_left == 0:
                    break

    return time_taken


# def reverseEvenLengthGroups(head):
#     total_grps = 0
#     curr_grp = 1
#     nodes_to_next_grp = 1
#     new_h = head

#     if not new_h.next:
#         return new_h

#     while new_h and new_h.next:
#         total_grps += 1
#         while nodes_to_next_grp > 0:
#             new_h = new_h.next
#             nodes_to_next_grp -= 1
#         nodes_to_next_grp =
#     print(total_grps)
#     # while new_h and new_h.next:
#     #     if curr_grp % 2 != 0:
#     #         curr_grp += 1
#     #         while nodes_to_next_grp > 0:
#     #             new_h = new_h.next
#     #             nodes_to_next_grp -= 1
#     #         nodes_to_next_grp = curr_grp
#     #     print(curr_grp)
#     #     curr_grp += 1

#     return new_h

# def preorderTraversal(root, vals = []):
#     if not root:
#         return


#     preorderTraversal(root.left, vals)
#     preorderTraversal(root.right, vals)
#     vals.append(root.val)
#     return vals


def levelOrderTraversal(root):
    if not root:
        return
    res = []
    queue = []
    levels = []
    queue.append(root)
    while len(queue) > 0:
        temp_node = queue.pop(0)
        levels.append(temp_node.val)

        if len(queue) == 0:
            res.append(levels)
            levels = []
        if temp_node.left:
            queue.append(temp_node.left)
        if temp_node.right:
            queue.append(temp_node.right)
    return res


def maxDistance(colors):
    max_dist = 0
    curr_idx = 0

    while curr_idx < len(colors):
        curr_color = colors[curr_idx]

        for idx, color in enumerate(colors):
            if color != curr_color:
                max_dist = max(max_dist, idx - curr_idx)

        curr_idx += 1
    return max_dist


def wateringPlants(plants, capacity):
    steps = 0
    curr_water = capacity
    for idx, plant in enumerate(plants):
        steps += 1

        if curr_water >= plant:
            curr_water -= plant
            continue

        if plant > curr_water:
            steps += idx
            curr_water = capacity
            steps += idx
            curr_water -= plant
            continue

    return steps


class RangeFreqQuery:
    def __init__(self, arr):
        self.loc = defaultdict(list)
        for i, x in enumerate(arr):
            self.loc[x].append(i)

    def query(self, left, right, value):
        if value not in self.loc:
            return 0
        lo = bisect_left(self.loc[value], left)
        hi = bisect_right(self.loc[value], right)
        return hi - lo


def targetIndices(nums, target):
    sorted_nums = sorted(nums)
    res = []
    for i, num in enumerate(sorted_nums):
        if num == target:
            res.append(i)

    return res


def getAverages(nums, k):
    res = []
    prev_sum = {}
    for i in range(len(nums)):
        if i - k < 0:
            res.append(-1)
            continue
        if i + k >= len(nums):
            res.append(-1)
            continue

        if (i - 1) in prev_sum:
            last_sum = prev_sum[i - 1]
            curr_sum = last_sum - nums[(i - k - 1)] + nums[i + k]
            curr_avg = curr_sum // (2 * k + 1)
            res.append(curr_avg)
            prev_sum[i] = curr_sum
            continue

        if i not in prev_sum:
            curr_sum = sum(nums[i - k : i + k + 1])
            curr_avg = curr_sum // (2 * k + 1)
            res.append(curr_avg)
            prev_sum[i] = curr_sum
            continue

    return res


def minimumDeletions(nums):
    if len(nums) == 1:
        return 1

    ans = 0
    mimimum_to_find_first = 0
    minimum, maximum = min(nums), max(nums)
    from_where_to_first = 0
    found_min, found_max = False, False

    queue = deque(nums)
    while queue:
        mimimum_to_find_first += 1
        val_left = queue.popleft()
        if val_left == minimum or val_left == maximum:
            from_where_to_first = 0
            if val_left == minimum:
                found_min = True
            else:
                found_max = True
            break
        val_right = queue.pop()
        if val_right == minimum or val_right == maximum:
            if val_right == minimum:
                found_min = True
            else:
                found_max = True
            from_where_to_first = 1
            break

    queue_after_first = deque(nums)
    if from_where_to_first == 0:
        for i in range(mimimum_to_find_first):
            queue_after_first.popleft()
    else:
        for i in range(mimimum_to_find_first):
            queue_after_first.pop()

    if found_min:
        target = maximum
    if found_max:
        target = minimum

    while queue_after_first:
        ans += 1
        val_left = queue_after_first.popleft()
        if val_left == target:
            break
        val_right = queue_after_first.pop()
        if val_right == target:
            break
    return ans + mimimum_to_find_first


def findAllPeople(n, meetings, firstPerson):
    knowers = {}
    ans = []
    for i in range(n):
        if i == 0:
            knowers[i] = [True, 0]
            continue
        if i == firstPerson:
            knowers[i] = [True, 0]
            continue
        knowers[i] = [False, 0]

    for i, meeting in enumerate(meetings):
        if knowers[meeting[0]][0] and knowers[meeting[0]][1] <= meeting[2]:
            knowers[meeting[1]][0] = True
            knowers[meeting[1]][1] = meeting[2]
            continue
        if knowers[meeting[1]][0] and knowers[meeting[1]][1] <= meeting[2]:
            knowers[meeting[0]] = True
            knowers[meeting[0]][1] = meeting[2]
            continue

    for person, knower in knowers.items():
        if knower[0]:
            ans.append(person)

    return ans


def firstPalindrome(words):
    def isPalindrome(word):
        i, j = 0, len(word) - 1
        while i <= j:
            if word[i] == word[j]:
                i += 1
                j -= 1
                continue
            return False
        return True

    for word in words:
        if isPalindrome(word):
            return word
    return ""


def addSpaces(s, spaces):
    spaces_len = len(spaces)
    space_idx = 0
    curr_space = spaces[space_idx]
    res = ""
    for i, l in enumerate(s):
        if i == curr_space:
            res += " "
            res += l
            space_idx += 1
            if space_idx < spaces_len:
                curr_space = spaces[space_idx]
            continue
        res += l
    return res


def getDescentPeriods(prices):
    n = len(prices)
    dp = [1] * n
    for i in range(1, n):
        if prices[i] == prices[i - 1] - 1:
            dp[i] = dp[i - 1] + 1
    return sum(dp)


def isSameAfterReversals(num: int) -> bool:
    num_str = str(num)

    if len(num_str) == 1:
        return True

    leading_zero = False
    temp = ""
    reversed1 = ""

    temp = num_str[::-1]

    for i, digit in enumerate(temp):
        if digit == "0" and i == 0:
            leading_zero = True
            continue

        if digit == "0" and leading_zero:
            continue

        if digit != "0" and leading_zero:
            leading_zero = False

        reversed1 += digit

    return num_str == reversed1[::-1]


def executeInstructions(n: int, startPos: List[int], s: str) -> List[int]:
    res = [0] * len(s)
    for i in range(len(res)):
        currentPos = startPos
        for _, ins in enumerate(s[i:]):
            if ins == "R":
                newLeft, newRight = currentPos[0], currentPos[1] + 1
                currentPos = [newLeft, newRight]
                if newLeft >= n or newRight >= n or newLeft < 0 or newRight < 0:
                    break

            if ins == "L":
                newLeft, newRight = currentPos[0], currentPos[1] - 1
                currentPos = [newLeft, newRight]
                if newLeft >= n or newRight >= n or newLeft < 0 or newRight < 0:
                    break

            if ins == "D":
                newLeft, newRight = currentPos[0] + 1, currentPos[1]
                currentPos = [newLeft, newRight]
                if newLeft >= n or newRight >= n or newLeft < 0 or newRight < 0:
                    break

            if ins == "U":
                newLeft, newRight = currentPos[0] - 1, currentPos[1]
                currentPos = [newLeft, newRight]
                if newLeft >= n or newRight >= n or newLeft < 0 or newRight < 0:
                    break
            res[i] += 1
    return res


def getDistances(arr: List[int]) -> List[int]:
    m, res = defaultdict(list), [0] * len(arr)
    for i, num in enumerate(arr):
        m[num].append(i)

    for _, l in m.items():
        prefix = []
        pn = len(l)
        for pos in l:
            prefix.append(pos if not prefix else prefix[-1] + pos)

        for i, v in enumerate(l):
            if i < pn - 1:
                # if it is not last element
                # muplitply current element times of number elements after it
                # and substract the sum of elements which are located after current
                res[v] += abs(v * (pn - i - 1) - (prefix[-1] - prefix[i]))
            if i > 0:
                # if it is not first element
                # do the same with number of element before current and their prefix sum
                res[v] += abs(v * i - prefix[i - 1])
    return res


def checkString(s: str) -> bool:
    bBefore = False
    for c in s:
        if c == "b":
            bBefore = True
        if c == "a" and bBefore:
            return False
    return True


def numberOfBeams(bank: List[str]) -> int:
    devices = defaultdict(int)
    for i, r in enumerate(bank):
        for c in r:
            if c == "1":
                devices[i] += 1
    res = 0
    a = list(devices.values())

    if len(a) <= 1:
        return res
    res = 0
    for i in range(1, len(a)):
        res += a[i] * a[i - 1]

    return res


def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    sAsteroids = sorted(asteroids)
    currMass = mass
    for ast in sAsteroids:
        if ast > currMass:
            return False

        currMass += ast

    return True


def maximumInvitations(favorite: List[int]) -> int:
    arrangements = defaultdict(list)
    for i, fav in enumerate(favorite):
        if arrangements[fav]:
            if len(arrangements[fav]) == 2:
                continue
            arrangements[fav].append(i)
            arrangements[i].append(fav)
            continue
        arrangements[i].append(fav)
    return arrangements


def checkValid(matrix: List[List[int]]) -> bool:
    columns = defaultdict(list)
    n = len(matrix[0])

    def isEqual(arr, n):
        return sorted(arr) == [x for x in range(1, n + 1)]

    for row in matrix:
        for i, v in enumerate(row):
            columns[i].append(v)
        if not isEqual(row, n):
            return False

    for col in columns.values():
        if not isEqual(col, n):
            return False

    return True


def minSwaps(nums: List[int]) -> int:
    nOnes, n = 0, len(nums)
    for i in range(0, n):
        if nums[i] == 1:
            nOnes += 1

    x, cOnes, maxOnes = nOnes, 0, 0

    for i in range(-1, x - 1):
        if nums[i] == 1:
            cOnes += 1

    maxOnes = cOnes

    for i in range(0, (n - x + 1)):
        if nums[i - 1] == 1:
            cOnes -= 1
        if nums[i + x - 1] == 1:
            cOnes += 1

        if maxOnes < cOnes:
            maxOnes = cOnes

    for i in range((n - x + 1), n):
        if nums[i - 1] == 1:
            cOnes -= 1
        if nums[(i + x - 1) - n] == 1:
            cOnes += 1
        if maxOnes < cOnes:
            maxOnes = cOnes

    res = x - maxOnes
    return res


def wordCount(startWords: List[str], targetWords: List[str]) -> int:
    res = 0

    def performConversation(word):
        conversed = []

        for l in string.ascii_lowercase:
            if l not in word:
                newWord = word + l
                conversed += ["".join(p) for p in permutations(newWord)]
        return conversed

    for target in targetWords:
        for start in startWords:
            times = 0
            queue = deque([start])
            while queue:
                word = queue.popleft()
                if word == target:
                    res += 1
                    continue
                if times == 0:
                    queue.extend(performConversation(word))
                    times += 1
    return res


def divideString(s: str, k: int, fill: str) -> List[str]:
    res = []
    n = len(s)
    for i in range(0, n, k):
        res.append(s[i : i + k])
    if len(res[-1]) < k:
        res[-1] += fill * (k - len(res[-1]))
    return res


class node:
    def __init__(self, val, level, doublesUsed):
        self.val = val
        self.level = level
        self.doublesUsed = doublesUsed


def minMoves(target: int, maxDoubles: int) -> int:
    # queue = deque([node(1, 0, 0)])
    # visited = set()
    # while queue:
    #     curr = queue.popleft()
    #     if curr.val == target:
    #         return curr.level

    #     visited.add(curr.val)

    #     if (
    #         curr.val * 2 == target and curr.doublesUsed < maxDoubles
    #     ) or curr.val + 1 == target:
    #         return curr.level + 1

    #     if curr.val + 1 not in visited and curr.val + 1 < target:
    #         queue.append(node(curr.val + 1, curr.level + 1, curr.doublesUsed))

    #     if (
    #         curr.val * 2 not in visited
    #         and curr.doublesUsed < maxDoubles
    #         and curr.val * 2 < target
    #     ):
    #         queue.append(node(curr.val * 2, curr.level + 1, curr.doublesUsed + 1))
    num, currDoubles, ans = target, maxDoubles, 0
    while num > 1:
        if num % 2 == 0 and currDoubles > 0:
            num //= 2
            currDoubles -= 1
            ans += 1
        else:

            if currDoubles == 0:
                return ans + num - 1
            num -= 1
            ans += 1
    return ans


def mostPoints(questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        currPoints, currBrainpower = questions[i]
        dp[i] = max(
            currPoints
            + (dp[i + currBrainpower + 1] if (i + currBrainpower + 1) < n else 0),
            dp[min(i + 1, n - 1)],
        )
    return dp[0]


def minimumCost(cost: List[int]) -> int:
    sorted_costs = sorted(cost, reverse=True)
    minimum_cost = 0
    for i, cost in enumerate(sorted_costs, start=1):
        if i % 3 != 0:
            minimum_cost += cost
    return minimum_cost


from itertools import accumulate


def numberOfArrays(differences: List[int], lower: int, upper: int) -> int:
    A = list(accumulate(differences, initial=0))
    return max(0, (upper - max(A)) + (min(A) - lower) + 1)


from collections import Counter


def countElements(nums: List[int]) -> int:
    c = Counter(nums)
    s = sorted(set(nums))
    res = 0
    for n in s[1:-1]:
        res += c[n]
    return res


def rearrangeArray(nums: List[int]) -> List[int]:
    pos = [i for i, x in enumerate(nums) if x > 0]
    neg = [i for i, x in enumerate(nums) if x < 0]
    res = []
    for p, n in zip(pos, neg):
        res.append(nums[p])
        res.append(nums[n])

    return res


def findFinalValue(nums: List[int], original: int) -> int:
    nextOriginal = original
    while nextOriginal in nums:
        nextOriginal = nextOriginal * 2
    return nextOriginal


def maxScoreIndices(nums: List[int]) -> List[int]:
    n, scores = len(nums), []
    ls, rs = 0, nums[0:n].count(1)
    scores.append(rs)

    for i in range(0, n):
        if nums[i] == 0:
            ls += 1
        if nums[i] == 1:
            rs -= 1
        scores.append(ls + rs)

    maxScore = max(scores)
    return [i for i, x in enumerate(scores) if x == maxScore]


def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    def getValue(s):
        return ord(s) - ord("a") + 1

    temp = 1
    for i in range(0, len(s) - k + 1):
        if i == 0:
            val = 0
            for j in range(k):
                val += getValue(s[j]) * temp

                temp *= power
        else:
            val -= getValue(s[i - 1])
            val += getValue(s[i + k - 1]) * temp
            val //= power
        ans = val % modulo
        if ans == hashValue:
            return s[i : i + k]


from itertools import zip_longest


def sortEvenOdd(nums: List[int]) -> List[int]:
    odds = [x for i, x in enumerate(nums) if i % 2 != 0]
    evens = [x for i, x in enumerate(nums) if i % 2 == 0]
    odds.sort(reverse=True)
    evens.sort()
    res = []
    print(evens)
    print(odds)
    for e, o in zip_longest(evens, odds):
        res.append(e)
        res.append(o)

    return [x for x in res if x is not None]


def smallestNumber(num: int) -> int:
    numList = list(str(num))
    if len(numList) == 1:
        return num
    counts = defaultdict(int)
    isNeg = False
    if numList[0] == "-":
        isNeg = True
        numList.pop(0)

    for num in numList:
        counts[int(num)] += 1

    res = ""
    if isNeg:
        vals = sorted(counts.keys(), reverse=True)
        for val in vals:
            res += str(val) * counts[val]
        return "-" + res

    vals = sorted(counts.keys())
    if vals[0] == 0:
        res += str(vals[1])
        counts[vals[1]] -= 1
    for val in vals:
        res += str(val) * counts[val]
    return res


class Bitset:
    def __init__(self, size: int):
        self.l = [0] * size
        self.ones = 0
        self.flipp = False

    def fix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 1:
                self.ones += 1
            self.l[idx] = 0
        else:
            if self.l[idx] == 0:
                self.ones += 1
            self.l[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 0:
                self.ones -= 1
            self.l[idx] = 1
        else:
            if self.l[idx] == 1:
                self.ones -= 1
            self.l[idx] = 0

    def flip(self) -> None:
        self.flipp = not self.flipp
        self.ones = len(self.l) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.l)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if not self.flipp:
            return "".join([str(i) for i in self.l])
        else:
            return "".join([str(0 if i else 1) for i in self.l])


def countOperations(num1: int, num2: int) -> int:
    ans = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        ans += 1
    return ans


def minimumOperations(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    length = len(nums)
    minSteps = float("inf")
    print(Counter(nums[::2]).most_common(2))
    print(Counter(nums[1::2]).most_common(2))
    for evenKey, evenVal in Counter(nums[::2]).most_common(2):
        for oddKey, oddVal in Counter(nums[1::2]).most_common(2):
            steps = length - evenVal if evenKey == oddKey else length - evenVal - oddVal
            minSteps = steps if steps < minSteps else minSteps
    return minSteps


def minimumRemoval(beans: List[int]) -> int:
    return sum(beans) - max((len(beans) - i) * n for i, n in enumerate(sorted(beans)))


if __name__ == "__main__":
    print(minimumRemoval([4, 1, 6, 5]))
    print(minimumRemoval([2, 10, 3, 2]))
