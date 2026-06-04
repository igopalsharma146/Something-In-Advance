def factorial(n, dp):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = n * factorial(n - 1, dp)
    return dp[n]

n = 500
dp = [-1] * (n + 1)

print(factorial(n, dp))