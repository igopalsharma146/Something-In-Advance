# Program: Search in Rotated Sorted Array (No Duplicates)

arr = list(map(int, input("Enter rotated sorted array: ").split()))
target = int(input("Enter target: "))


# Brute Force Approach
index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print("\nBrute Force Approach")
print("Index:", index)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
temp = sorted(arr)

left = 0
right = len(temp) - 1
found = False

while left <= right:

    mid = (left + right) // 2

    if temp[mid] == target:
        found = True
        break

    elif temp[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if found:
    index = arr.index(target)
else:
    index = -1

print("\nBetter Approach")
print("Index:", index)

print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")


# Optimal Approach
left = 0
right = len(arr) - 1

index = -1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        index = mid
        break

    # Left half sorted
    if arr[left] <= arr[mid]:

        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Right half sorted
    else:

        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1

print("\nOptimal Approach")
print("Index:", index)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")