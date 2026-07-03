# Program: N-Queen Problem (Optimized Backtracking)

n = int(input("Enter value of N: "))
board = [["." for _ in range(n)] for _ in range(n)]

# Hash Arrays
leftRow = [0] * n
upperDiagonal = [0] * (2 * n - 1)
lowerDiagonal = [0] * (2 * n - 1)
result = []


def solve(col):
    # Base Case
    if col == n:
        temp = []

        for row in board:
            temp.append("".join(row))
        result.append(temp)
        return

    for row in range(n):
        if (leftRow[row] == 0 and
            lowerDiagonal[row + col] == 0 and
            upperDiagonal[row - col + n - 1] == 0):

            # Place Queen
            board[row][col] = "Q"
            leftRow[row] = 1
            lowerDiagonal[row + col] = 1
            upperDiagonal[row - col + n - 1] = 1
            solve(col + 1)

            # Backtrack
            board[row][col] = "."
            leftRow[row] = 0
            lowerDiagonal[row + col] = 0
            upperDiagonal[row - col + n - 1] = 0

solve(0)
print("\nOptimal Approach")

for solution in result:
    for row in solution:
        print(row)
    print()

print("Total Solutions:", len(result))
print("Time Complexity: O(N!)")
print("Space Complexity: O(N²)")