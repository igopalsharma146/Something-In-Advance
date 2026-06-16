# Program: Find Minimum in Rotated Sorted Array

arr = list(map(int, input("Enter rotated sorted array: ").split()))


# Brute Force Approach
minimum = min(arr)

print("\nBrute Force Approach")
print("Minimum Element:", minimum)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num

print("\nBetter Approach")
print("Minimum Element:", minimum)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Optimal Approach
left = 0
right = len(arr) - 1

minimum = float('inf')

while left <= right:

    # Entire search space sorted
    if arr[left] <= arr[right]:
        minimum = min(minimum, arr[left])
        break

    mid = (left + right) // 2

    # Left half sorted
    if arr[left] <= arr[mid]:

        minimum = min(minimum, arr[left])
        left = mid + 1

    # Right half sorted
    else:

        minimum = min(minimum, arr[mid])
        right = mid - 1

print("\nOptimal Approach")
print("Minimum Element:", minimum)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")