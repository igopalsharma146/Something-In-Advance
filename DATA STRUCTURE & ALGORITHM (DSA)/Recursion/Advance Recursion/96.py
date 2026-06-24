# Program: Count All Subsequences With Sum = K

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))


# Brute Force Approach (Generate All Subsequences)

count = 0
n = len(arr)

for mask in range(1 << n):
    total = 0

    for i in range(n):
        if mask & (1 << i):
            total += arr[i]

    if total == k:
        count += 1

print("\nBrute Force Approach")
print("Count of Subsequences:", count)

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(1)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Recursion)

def solve(index, total):

    if index == len(arr):
        if total == k:
            return 1
        return 0

    # Take current element
    left = solve(index + 1,total + arr[index])

    # Not Take current element
    right = solve(index + 1,total)
    return left + right


count = solve(0, 0)

print("\nOptimal Approach")
print("Count of Subsequences:", count)

print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")