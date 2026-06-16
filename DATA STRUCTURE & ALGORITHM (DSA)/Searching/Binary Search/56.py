# Program: Find Floor and Ceil in a Sorted Array

# CEIL= smallest number in an array >= target
# Floor= largest number in an array <= target

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))


# Brute Force Approach
floor_value = -1
ceil_value = -1

for num in arr:

    if num <= target:
        floor_value = num

    if ceil_value == -1 and num >= target:
        ceil_value = num

print("\nBrute Force Approach")
print("Floor:", floor_value)
print("Ceil :", ceil_value)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
floor_value = -1
ceil_value = -1

# Floor
left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] <= target:
        floor_value = arr[mid]
        left = mid + 1
    else:
        ceil_value = arr[mid]
        right = mid - 1 


# # Ceil
# left = 0
# right = len(arr) - 1

# while left <= right:

#     mid = (left + right) // 2

#     if arr[mid] >= target:
        # ceil_value = arr[mid]
#         right = mid - 1
#     else:
#         left = mid + 1

print("\nBetter Approach")
print("Floor:", floor_value)
print("Ceil :", ceil_value)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

