# Program: Count Occurrences of a Number in Sorted Array

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))


# Brute Force Approach
count = 0
for num in arr:
    if num == target:
        count += 1

print("\nBrute Force Approach")
print("Count:", count)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
first = -1
last = -1

# First Occurrence
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        first = mid
        right = mid - 1

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


# Last Occurrence
left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        last = mid
        left = mid + 1

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


if first == -1:
    count = 0
else:
    count = last - first + 1

print("\nBetter Approach")
print("Count:", count)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


lb = lower_bound(arr, target)

if lb == len(arr) or arr[lb] != target:
    count = 0
else:
    ub = upper_bound(arr, target)
    count = ub - lb

print("\nOptimal Approach")
print("Count:", count)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")