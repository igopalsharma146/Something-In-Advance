# Program: Best Time to Buy and Sell Stock

arr = list(map(int, input("Enter stock prices separated by space: ").split()))


# Brute Force Approach
max_profit = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        profit = arr[j] - arr[i]

        if profit > max_profit:
            max_profit = profit

print("\nBrute Force Approach")
print("Maximum Profit:", max_profit)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
max_profit = 0

for i in range(len(arr)):
    min_price = arr[i]

    for j in range(i + 1, len(arr)):
        profit = arr[j] - min_price
        max_profit = max(max_profit, profit)

print("\nBetter Approach")
print("Maximum Profit:", max_profit)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Optimal Approach
min_price = arr[0]
max_profit = 0

for i in range(1, len(arr)):

    profit = arr[i] - min_price
    max_profit = max(max_profit, profit)

    min_price = min(min_price, arr[i])

print("\nOptimal Approach")
print("Maximum Profit:", max_profit)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")