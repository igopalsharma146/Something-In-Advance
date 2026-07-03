# Program: Letter Combinations of a Phone Number

digits = input("Enter Digits (2-9): ")


# Brute Force Approach

print("\nBrute Force Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)

print("\nOptimal Approach")

phone = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

result = []
def solve(index, current):
    if index == len(digits):
        result.append(current)
        return

    letters = phone[digits[index]]
    for ch in letters:
        solve(index + 1, current + ch)

if digits:
    solve(0, "")
print(result)

print("Time Complexity: O(4^N × N)")
print("Space Complexity: O(N)")

    #              ""
    #       /       |       \
    #      a        b        c
    #   / | \    / | \    / | \
    #  d  e  f  d  e  f  d  e  f