# dynamic programming are used to save time but it takes memory
#it will take high amount of time
print("\n")
def fib(num):
    if num==1:
        return 0
    if num==2:
        return 1
    return fib(num-2)+fib(num-1)
# for i in range(1,1000):
    # print(fib(i))
    
print("\n")
def fibonacci(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)
    return dp[n]

n = 100
dp = [-1] * (n + 1)
print(dp)

print(fibonacci(n, dp))