# Program: Right Rotate Array by One Place

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
rotated = [0] * len(arr)

rotated[0] = arr[-1]

for i in range(len(arr) - 1):
    rotated[i + 1] = arr[i]

print("\nBrute Force Approach")
print("Array after right rotation:", rotated)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach
temp = arr.copy()

last = temp[-1]

for i in range(len(temp) - 1, 0, -1):
    temp[i] = temp[i - 1]

temp[0] = last

print("\nBetter Approach")
print("Array after right rotation:", temp)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")