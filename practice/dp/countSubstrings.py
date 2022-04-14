def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        count = 1
        for j in range(0, i):
            if s[0 : j + 1] == s[j::-1]:
                count += 1
        dp[i] = dp[i - 1] + count
        count = 0
    return dp[n - 1]


if __name__ == "__main__":
    print(countSubstrings("abc"))
    print(countSubstrings("aaa"))
