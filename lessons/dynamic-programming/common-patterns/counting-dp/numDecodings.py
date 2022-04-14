from collections import defaultdict


def numDecodings(s: str) -> int:
    cache = defaultdict(int)

    def dp(i):
        if i in cache:
            return cache[i]
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        res = dp(i + 1)
        if i + 1 < len(s) and (10 <= int(s[i : i + 2]) <= 26):
            res += dp(i + 2)

        return res

    return dp(0)


if __name__ == "__main__":
    print(numDecodings(s="12"))
    print(numDecodings(s="226"))
    print(numDecodings(s="06"))
