# Program: Maximum Consecutive Ones

arr = list(map(int, input("Enter array elements (0s and 1s) separated by space: ").split()))


# Brute Force Approach
max_count = 0

for i in range(len(arr)):

    if arr[i] == 1:
        count = 0

        for j in range(i, len(arr)):
            if arr[j] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                break

print("\nBrute Force Approach")
print("Maximum Consecutive Ones:", max_count)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
max_count = 0

for i in range(len(arr)):
    count = 0

    if arr[i] == 1:
        j = i

        while j < len(arr) and arr[j] == 1:
            count += 1
            j += 1

        max_count = max(max_count, count)

print("\nBetter Approach")
print("Maximum Consecutive Ones:", max_count)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Optimal Approach
count = 0
max_count = 0

for num in arr:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print("\nOptimal Approach")
print("Maximum Consecutive Ones:", max_count)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")