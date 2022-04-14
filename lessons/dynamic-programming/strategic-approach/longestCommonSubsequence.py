from collections import defaultdict


def longestCommonSubsequence(text1: str, text2: str) -> int:
    cache = defaultdict(int)

    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if text1[i - 1] == text2[j - 1]:
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = dp(i - 1, j - 1) + 1
            return cache[(i, j)]

        if (i, j) in cache:
            return cache[(i, j)]
        cache[(i, j)] = max(dp(i, j - 1), dp(i - 1, j))
        return cache[(i, j)]

    i, j = len(text1), len(text2)
    return dp(i, j)

    # Botton-up iterative
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    print(longestCommonSubsequence(text1="abcde", text2="ace"))
    print(longestCommonSubsequence(text1="abc", text2="abc"))
    print(longestCommonSubsequence(text1="abc", text2="def"))
