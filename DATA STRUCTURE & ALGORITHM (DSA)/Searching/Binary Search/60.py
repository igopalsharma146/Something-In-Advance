# Program: Search in Rotated Sorted Array (Duplicates Allowed)

arr = list(map(int, input("Enter rotated sorted array: ").split()))
target = int(input("Enter target: "))


# Brute Force Approach
index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print("\nBrute Force Approach")
print("Found" if index != -1 else "Not Found")

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

print("\nBetter Approach")
print("Found" if found else "Not Found")

print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")


# Optimal Approach
left = 0
right = len(arr) - 1

found = False

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        found = True
        break

    # Duplicate case
    if arr[left] == arr[mid] == arr[right]:
        left += 1
        right -= 1
        continue

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
print("Found" if found else "Not Found")

print("Time Complexity: O(log n) Average Case")
print("Time Complexity: O(n) Worst Case")
print("Space Complexity: O(1)")