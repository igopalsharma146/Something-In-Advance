# Program: Find the Missing Number in an Array

arr = list(map(int, input("Enter array elements separated by space: ").split()))

n = len(arr) + 1


# Brute Force Approach
missing = -1

for i in range(1, n + 1):
    if i not in arr:
        missing = i
        break

print("\nBrute Force Approach")
print("Missing Number:", missing)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
hash_map = [0] * (n + 1)

for num in arr:
    hash_map[num] = 1

missing = -1

for i in range(1, n + 1):
    if hash_map[i] == 0:
        missing = i
        break

print("\nBetter Approach")
print("Missing Number:", missing)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum

print("\nOptimal Approach")
print("Missing Number:", missing)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")