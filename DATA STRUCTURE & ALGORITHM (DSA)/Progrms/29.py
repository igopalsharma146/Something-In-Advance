# Program: Check if an Array is Sorted or Not

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
sorted_arr = sorted(arr)

print("\nBrute Force Approach")

if arr == sorted_arr:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")

print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")


# Better Approach
is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print("\nBetter Approach")

if is_sorted:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")