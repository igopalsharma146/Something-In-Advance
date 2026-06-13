# Program: Linear Search

arr = list(map(int, input("Enter array elements separated by space: ").split()))
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
try:
    index = arr.index(target)

    print("\nBetter Approach")
    print(f"Element found at index {index}")

except ValueError:

    print("\nBetter Approach")
    print("Element not found")

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Brute Force Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")