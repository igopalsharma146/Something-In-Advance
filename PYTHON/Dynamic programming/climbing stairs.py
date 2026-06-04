def climb(n, dp):
    if n <= 2:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = climb(n - 1, dp) + climb(n - 2, dp)
    return dp[n]

n = 5
dp = [-1] * (n + 1)

print(climb(n, dp))