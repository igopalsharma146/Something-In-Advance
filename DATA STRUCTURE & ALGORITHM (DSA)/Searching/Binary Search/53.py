# Binary search

# 1. Real Life Example

# Suppose tum dictionary me word search kar rahe ho:
# APPLE
# BALL
# CAT
# DOG
# ELEPHANT
# FISH
# GOAT
# HORSE
# ...

# Agar tumhe GOAT dhoondhna hai to:
# Middle page kholo
# Agar GOAT middle word se bada hai → right side jao
# Chhota hai → left side jao

# Har step me aadhi dictionary eliminate ho jaati hai.
# Yehi Binary Search hai.
# Condition: Data Sorted hona chahiye.


# 2. Coding Problem

# Given a sorted array:
# arr = [2, 4, 6, 8, 10, 12, 14]

# Find:
# target = 10

# Output:
# Element found at index 4



# 3. Iterative Solution
# Program: Binary Search (Iterative)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    return -1


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")



# 4. Recursive solution
# Program: Binary Search (Recursive)
print("\nBinary Search (Recursive Solution) :")
def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)

    else:
        return binary_search(arr, left, mid - 1, target)


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# 5. Time & Space Complexity

# Iterative Binary Search
# Complexity	Value
# Time Complexity	O(log n)
# Space Complexity	O(1)

# Recursive Binary Search
# Complexity	Value
# Time Complexity	O(log n)
# Space Complexity	O(log n)