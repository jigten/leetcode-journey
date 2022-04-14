from functools import lru_cache
from typing import List


def generateParenthesis(n: int) -> List[str]:
    @lru_cache(None)
    def dp(i):
        if i == 0:
            return [""]
        if i == 1:
            return ["()"]

        return [
            "(" + preStr + ")" + postStr
            for j in range(i)
            for preStr in dp(j)
            for postStr in dp(i - 1 - j)
        ]

    return dp(n)


if __name__ == "__main__":
    print(generateParenthesis(n=3))
    print(generateParenthesis(n=2))
    print(generateParenthesis(n=1))
