# Program: N-Queens Problem

n = int(input("Enter the value of N: "))

# Brute Force Approach

print("\nBrute Force Approach")
print("Not Applicable")

print("Time Complexity: O(N^N)")
print("Space Complexity: O(N^2)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)

print("\nOptimal Approach")
board = [["." for _ in range(n)] for _ in range(n)]
result = []

def is_safe(row, col):

    # Check Upper Left Diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check Same Column
    i = row - 1
    while i >= 0:
        if board[i][col] == "Q":
            return False
        i -= 1

    # Check Upper Right Diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    if row == n:
        temp = []

        for r in board:
            temp.append("".join(r))
        result.append(temp)
        return

    for col in range(n):
        if is_safe(row, col):
            board[row][col] = "Q"
            solve(row + 1)
            board[row][col] = "."

solve(0)

for solution in result:
    for row in solution:
        print(row)
    print()

print("Total Solutions:", len(result))

print("Time Complexity: O(N!)")
print("Space Complexity: O(N^2)")