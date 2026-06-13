# Program: Merge Two Sorted Arrays

arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))


# Brute Force Approach
merged = arr1 + arr2
merged.sort()

print("\nBrute Force Approach")
print("Merged Array:", merged)
print("Time Complexity: O((n+m) log(n+m))")
print("Space Complexity: O(n+m)")


# Better Approach
merged = []
i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("\nBetter Approach")
print("Merged Array:", merged)
print("Time Complexity: O(n+m)")
print("Space Complexity: O(n+m)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n+m)")
print("Space Complexity: O(n+m)")