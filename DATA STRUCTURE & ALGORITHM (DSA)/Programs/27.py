# Program: Find Largest Element in an Array

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
sorted_arr = sorted(arr)

print("\nBrute Force Approach")
print("Largest Element:", sorted_arr[-1])
print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")


# Better Approach
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("\nBetter Approach")
print("Largest Element:", largest)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")