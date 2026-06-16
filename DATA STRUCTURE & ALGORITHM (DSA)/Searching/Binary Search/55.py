# Program: Search Insert Position

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))


# Brute Force Approach
position = len(arr)

for i in range(len(arr)):
    if arr[i] >= target:
        position = i
        break

print("\nBrute Force Approach")
print("Insert Position:", position)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
position = len(arr)
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] >= target:
        position = mid # hum lower bound ki position per insert kar rahe h
        right = mid - 1
    else:
        left = mid + 1

print("\nBetter Approach")
print("Insert Position:", position)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")