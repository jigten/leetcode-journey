from functools import lru_cache
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    # n = len(s)
    # dp = [False] * n
    # for i in range(n):
    #     for word in wordDict:
    #         if i >= len(word) - 1:
    #             if s[i - len(word) + 1 : i + 1] == word and (
    #                 i == len(word) - 1 or dp[i - len(word)]
    #             ):
    #                 dp[i] = True
    # return dp[n - 1]
    @lru_cache(None)
    def dp(i):
        for word in wordDict:
            word_length = len(word)
            if s[i - word_length + 1 : i + 1] == word:
                if i == word_length - 1 or dp(i - word_length):
                    return True
        return False

    return dp(len(s) - 1)


if __name__ == "__main__":
    print(wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
