# Program: Rat In A Maze

n = int(input("Enter size of maze: "))
maze = []

print("Enter Maze (0 = Blocked, 1 = Open Path)")
for i in range(n):
    maze.append(list(map(int, input().split())))


# Brute Force Approach

print("\nBrute Force Approach")
print("Not Applicable")

print("Time Complexity: Exponential")
print("Space Complexity: O(N²)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)

print("\nOptimal Approach")
result = []
visited = [[0 for _ in range(n)] for _ in range(n)]

def solve(row, col, path):

    # Destination Reached
    if row == n - 1 and col == n - 1:
        result.append(path)
        return
    visited[row][col] = 1

    # Down
    if (row + 1 < n and
        maze[row + 1][col] == 1 and
        visited[row + 1][col] == 0):
        solve(row + 1, col, path + "D")

    # Left
    if (col - 1 >= 0 and
        maze[row][col - 1] == 1 and
        visited[row][col - 1] == 0):
        solve(row, col - 1, path + "L")

    # Right
    if (col + 1 < n and
        maze[row][col + 1] == 1 and
        visited[row][col + 1] == 0):
        solve(row, col + 1, path + "R")

    # Up
    if (row - 1 >= 0 and
        maze[row - 1][col] == 1 and
        visited[row - 1][col] == 0):
        solve(row - 1, col, path + "U")
    visited[row][col] = 0


if maze[0][0] == 1:
    solve(0, 0, "")
print(result)

print("Time Complexity: O(4^(N²))")
print("Space Complexity: O(N²)")