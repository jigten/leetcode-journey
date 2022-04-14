from functools import lru_cache
from typing import List


def minDifficulty(jobDifficulty: List[int], d: int) -> int:
    n = len(jobDifficulty)
    if n < d:
        return -1

    hardest_job_left = [0] * n
    hardest_job = 0
    for i in range(n - 1, -1, -1):
        hardest_job = max(hardest_job, jobDifficulty[i])
        hardest_job_left[i] = hardest_job

    @lru_cache(None)
    def dp(i, day):
        if day == d:
            return hardest_job_left[i]
        best = float("inf")

        for k in range(i, n - (d - day)):
            best = min(best, max(jobDifficulty[i : k + 1]) + dp(k + 1, day + 1))
        return best

    return dp(0, 1)

    n = len(jobDifficulty)
    if n < d:
        return -1

    dp = [[float("inf")] * (d + 1) for _ in range(n)]

    # Set base cases
    dp[-1][d] = jobDifficulty[-1]

    # On the last day, we must schedule all remaining jobs, so dp[i][d]
    # is the maximum difficulty job remaining
    for i in range(n - 2, -1, -1):
        dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])

    for day in range(d - 1, 0, -1):
        for i in range(day - 1, n - (d - day)):
            hardest = 0
            # Iterate through the options and choose the best
            for j in range(i, n - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                # Recurrence relation
                dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

    return dp[0][1]


if __name__ == "__main__":
    print(minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
    print(minDifficulty(jobDifficulty=[9, 9, 9], d=4))
