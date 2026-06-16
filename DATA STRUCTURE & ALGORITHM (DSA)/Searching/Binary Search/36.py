# Program: Binary Search
# Condition: Array sorted hona chahiye
arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))
target = int(input("Enter element to search: "))


# Brute Force Approach
index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print("\nBrute Force Approach")

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
left = 0
right = len(arr) - 1
index = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        index = mid
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print("\nBetter Approach")

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")