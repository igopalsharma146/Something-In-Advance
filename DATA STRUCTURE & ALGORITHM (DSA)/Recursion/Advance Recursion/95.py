# Program: Check If There Exists A Subsequence With Sum = K

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))


# Brute Force Approach (Generate All Subsequences)

exist = False
n = len(arr)

for mask in range(1 << n):
    total = 0

    for i in range(n):
        if mask & (1 << i):
            total += arr[i]

    if total == k:
        exist = True
        break

print("\nBrute Force Approach")
print("Subsequence Exists:", exist)

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(1)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Recursion + Early Return)
def solve(index, total):
    if total == k:
        return True

    if index >= len(arr):
        return False

    # Take current element
    if solve(index + 1, total + arr[index]):
        return True

    # Not Take current element
    if solve(index + 1, total):
        return True
    return False
answer = solve(0, 0)

print("\nOptimal Approach")
print("Subsequence Exists:", answer)

print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")