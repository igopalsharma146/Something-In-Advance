# Program: Subset Sum - I

arr = list(map(int, input("Enter array elements: ").split()))

# Brute Force Approach (Bit Manipulation)
print("\nBrute Force Approach")
result = []
n = len(arr)

for mask in range(1 << n):
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += arr[i]

    result.append(total)

result.sort()
print(result)

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(2^N)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)

print("\nOptimal Approach")
result = []

def solve(index, total):
    if index == len(arr):
        result.append(total)
        return

    # Take
    solve(index + 1, total + arr[index])

    # Not Take
    solve(index + 1, total)

solve(0, 0)
result.sort()
print(result)

print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")


    #              (0)
    #            /     \
    #        +2         Skip2
    #       (2)          (0)
    #      /   \        /   \
    #   +3     Skip3  +3   Skip3
    #  (5)      (2)   (3)    (0)