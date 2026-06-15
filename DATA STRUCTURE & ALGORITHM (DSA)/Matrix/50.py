# Program: Generate Spiral Matrix

n = int(input("Enter matrix size: "))


# Brute Force Approach

matrix = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

print("\nBrute Force Approach")

for row in matrix:
    print(row)

print("Time Complexity: O(n²)")
print("Space Complexity: O(n²)")


# Better Approach

print("\nBetter Approach")
print("Optimal Solution is same as Brute Force Solution.")
print("Time Complexity: O(n²)")
print("Space Complexity: O(n²)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Brute Force Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n²)")
print("Space Complexity: O(n²)")