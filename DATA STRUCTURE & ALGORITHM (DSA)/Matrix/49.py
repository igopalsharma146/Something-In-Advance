# Program: Spiral Matrix Traversal

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


# Brute Force Approach
row = len(matrix)
col = len(matrix[0])

visited = [[False] * col for _ in range(row)]

result = []

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r = 0
c = 0
direction = 0

for _ in range(row * col):

    result.append(matrix[r][c])
    visited[r][c] = True

    nr = r + dr[direction]
    nc = c + dc[direction]

    if (0 <= nr < row and
        0 <= nc < col and
        not visited[nr][nc]):

        r = nr
        c = nc

    else:
        direction = (direction + 1) % 4
        r += dr[direction]
        c += dc[direction]

print("\nBrute Force Approach")
print("Spiral Traversal:", result)
print("Time Complexity: O(m*n)")
print("Space Complexity: O(m*n)")


# Better Approach
top = 0
bottom = row - 1
left = 0
right = col - 1

result = []

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print("\nBetter Approach")
print("Spiral Traversal:", result)
print("Time Complexity: O(m*n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(m*n)")
print("Space Complexity: O(1)")