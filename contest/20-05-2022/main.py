from functools import lru_cache
from typing import List


def countHillValley(nums: List[int]) -> int:
    res = 0
    for i in range(1, len(nums) - 1):
        curr_val = nums[i]
        next_val = nums[i + 1]
        prev_val = nums[i - 1]
        for j in range(i - 1, -1, -1):
            if nums[j] != nums[i]:
                prev_val = nums[j]
                break
        for k in range(i + 1, len(nums)):
            if nums[k] != nums[i]:
                next_val = nums[k]
                break
        if prev_val < curr_val > next_val:
            if curr_val == nums[i - 1]:
                continue
            res += 1
        if prev_val > curr_val < next_val:
            if curr_val == nums[i - 1]:
                continue
            res += 1
    return res


def countCollisions(directions: str) -> int:
    res = 0
    dirs = list(directions)
    chain_r = 0
    for i in range(1, len(dirs)):
        if dirs[i] == "L" and dirs[i - 1] == "R":
            res += 2
            res += chain_r
            chain_r = 0
            dirs[i] = "C"
        if dirs[i] == "L" and (dirs[i - 1] == "S" or dirs[i - 1] == "C"):
            res += 1
            dirs[i] = "C"
            res += chain_r
            chain_r = 0
        if dirs[i] == "S" and dirs[i - 1] == "R":
            res += 1
            dirs[i] = "C"
            res += chain_r
            chain_r = 0
        if dirs[i] == "R" and dirs[i - 1] == "R":
            chain_r += 1
    return res


def maximumBobPoints(numArrows: int, aliceArrows: List[int]) -> List[int]:
    rounds = len(aliceArrows)

    def backtrack(index, remaining, cur_max, cur_game):
        if index < 0 or remaining == 0:
            nonlocal max_points, bob_arrows
            if cur_max > max_points:
                max_points = cur_max
                bob_arrows = cur_game[:]
                if remaining > 0:
                    bob_arrows[0] += remaining
            return

        if remaining > aliceArrows[index]:
            cur_game[index] = aliceArrows[index] + 1
            backtrack(
                index - 1, remaining - aliceArrows[index] - 1, cur_max + index, cur_game
            )

        cur_game[index] = 0
        backtrack(index - 1, remaining, cur_max, cur_game)

    bob_arrows = [0] * rounds
    max_points = 0
    backtrack(rounds - 1, numArrows, 0, [0] * rounds)
    return bob_arrows


if __name__ == "__main__":
    # print(
    #     maximumBobPoints(numArrows=9, aliceArrows=[1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0])
    # )
    print(
        maximumBobPoints(numArrows=3, aliceArrows=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2])
    )
