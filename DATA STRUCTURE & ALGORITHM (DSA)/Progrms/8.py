# Program: Print Frequency of Elements in an Array

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
print("\nBrute Force Approach")

visited = []

for i in range(len(arr)):
    if arr[i] in visited:
        continue

    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    visited.append(arr[i])
    print(f"{arr[i]} -> {count}")

print("Time Complexity: O(n²)")
print("Space Complexity: O(n)")


# Better Approach
print("\nBetter Approach")

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key, value in freq.items():
    print(f"{key} -> {value}")

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")