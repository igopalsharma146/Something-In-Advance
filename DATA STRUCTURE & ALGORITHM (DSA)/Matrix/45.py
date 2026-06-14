# Program: Print Upper Triangle, Lower Triangle and Both Diagonals

nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

n = len(nums)


# Upper Triangle
print("\nUpper Triangle")

for i in range(n):
    for j in range(n):
        if i <= j:
            print(nums[i][j], end=" ")
    print()
print("Time Complexity: O(n²) \nSpace Complexity: O(1)")


# Lower Triangle
print("\nLower Triangle")

for i in range(n):
    for j in range(n):
        if i >= j:
            print(nums[i][j], end=" ")
    print()
print("Time Complexity: O(n²) \nSpace Complexity: O(1)")


# Primary Diagonal
print("\nPrimary Diagonal")

for i in range(n):
    print(nums[i][i], end=" ")
print("Time Complexity: O(n) \nSpace Complexity: O(1)")


# Secondary Diagonal
print("\n\nSecondary Diagonal")

for i in range(n):
    print(nums[i][n - 1 - i], end=" ")
print("Time Complexity: O(n) \nSpace Complexity: O(1)")


# Both Diagonals
print("\n\nBoth Diagonals")

for i in range(n):
    for j in range(n):

        if i == j or i + j == n - 1:
            print(nums[i][j], end=" ")

print()
print("Time Complexity: O(n²) \nSpace Complexity: O(1)")
