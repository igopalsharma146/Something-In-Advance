# Program: Rotate Matrix by 90 Degrees Clockwise

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Brute Force Approach
n = len(matrix)

rotated = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated[j][n - 1 - i] = matrix[i][j]

print("\nBrute Force Approach")
for row in rotated:
    print(row)

print("Time Complexity: O(n²)")
print("Space Complexity: O(n²)")


# Better Approach
temp = [row[:] for row in matrix]

# Transpose
for i in range(n):
    for j in range(n):
        temp[j][i] = matrix[i][j]

# Reverse each row
for row in temp:
    row.reverse()

print("\nBetter Approach")
for row in temp:
    print(row)

print("Time Complexity: O(n²)")
print("Space Complexity: O(n²)")


# Optimal Approach
temp = [row[:] for row in matrix]

# Transpose
for i in range(n):
    for j in range(i + 1, n):
        temp[i][j], temp[j][i] = temp[j][i], temp[i][j]

# Reverse each row
for row in temp:
    left = 0
    right = n - 1

    while left < right:
        row[left], row[right] = row[right], row[left]
        left += 1
        right -= 1

print("\nOptimal Approach")
for row in temp:
    print(row)

print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")