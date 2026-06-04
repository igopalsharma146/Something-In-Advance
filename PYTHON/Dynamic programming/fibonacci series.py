def fibonacci(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)
    return dp[n]

n = 100
dp = [-1] * (n + 1)

for i in range(n + 1):
    print(fibonacci(i, dp), end=" ")