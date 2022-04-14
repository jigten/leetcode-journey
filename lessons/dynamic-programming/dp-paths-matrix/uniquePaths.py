def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m][n]


if __name__ == "__main__":
    print(uniquePaths(m=3, n=7))
    print(uniquePaths(m=3, n=2))
