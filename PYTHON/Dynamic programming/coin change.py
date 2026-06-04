def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    # print(dp)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                print(dp)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5, 10]
amount = 57

print(coin_change(coins, amount))