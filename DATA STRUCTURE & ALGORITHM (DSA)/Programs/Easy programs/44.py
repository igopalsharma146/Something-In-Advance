# Program: Maximum Subarray Sum

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
max_sum = float('-inf')

for i in range(len(arr)):

    current_sum = 0

    for j in range(i, len(arr)):
        current_sum += arr[j]
        max_sum = max(max_sum, current_sum)

print("\nBrute Force Approach")
print("Maximum Subarray Sum:", max_sum)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

max_sum = float('-inf')

for i in range(len(arr)):
    for j in range(i, len(arr)):

        if i == 0:
            current_sum = prefix[j]
        else:
            current_sum = prefix[j] - prefix[i - 1]

        max_sum = max(max_sum, current_sum)

print("\nBetter Approach")
print("Maximum Subarray Sum:", max_sum)
print("Time Complexity: O(n²)")
print("Space Complexity: O(n)")


# Optimal Approach
current_sum = 0
max_sum = float('-inf')

for num in arr:

    current_sum += num

    max_sum = max(max_sum, current_sum)

    if current_sum < 0:
        current_sum = 0

print("\nOptimal Approach")
print("Maximum Subarray Sum:", max_sum)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")