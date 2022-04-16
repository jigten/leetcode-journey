import sys
from typing import List


def findClosestNumber(nums: List[int]) -> int:
    min_dist, closest_num = float("inf"), 0
    for num in nums:
        dist = abs(num)
        if dist < min_dist:
            min_dist = dist
            closest_num = num
        if dist == min_dist:
            if num > closest_num:
                closest_num = num

    return closest_num


def waysToBuyPensPencils(total: int, cost1: int, cost2: int) -> int:
    """
    You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.
    Return the number of distinct ways you can buy some number of pens and pencils.
    """
    if total < cost1 and total < cost2:
        return 1

    if total < cost1:
        return total // cost2 + 1

    if total < cost2:
        return total // cost1 + 1

    count = 0
    waysToBuyPen = total // cost1
    for i in range(0, waysToBuyPen + 1):
        costLeft = total - (cost1 * i)
        count += costLeft // cost2 + 1
    return count


class ATM:
    def __init__(self):
        self.banknotes = [0] * 5
        self.noteValues = {0: 500, 1: 200, 2: 100, 3: 50, 4: 20}

    def deposit(self, banknotesCount: List[int]) -> None:
        newBankNotes = [x + y for x, y in zip(reversed(banknotesCount), self.banknotes)]

        self.banknotes = newBankNotes

    def withdraw(self, amount: int) -> List[int]:
        results = [0] * 5
        amountLeft = amount
        transactions = [0] * 5

        for i, noteCount in enumerate(self.banknotes):
            if noteCount > 0:
                noteVal = self.noteValues[i]
                maxNotes = amountLeft // noteVal
                if noteCount > maxNotes:
                    results[i] = maxNotes
                    amountLeft -= maxNotes * noteVal
                    transactions[i] -= maxNotes
                else:
                    results[i] = noteCount
                    amountLeft -= noteCount * noteVal
                    transactions[i] -= noteCount

        if amountLeft > 0:
            return [-1]
        newBankNotes = [x + y for x, y in zip(transactions, self.banknotes)]
        self.banknotes = newBankNotes
        return list(reversed(results))


atm = ATM()
atm.deposit([0, 0, 1, 2, 1])
print(atm.withdraw(600))
atm.deposit([0, 1, 0, 1, 1])
print(atm.withdraw(600))
print(atm.withdraw(550))
