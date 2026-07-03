# Program: Combination Sum - III

k = int(input("Enter number of elements (k): "))
target = int(input("Enter Target Sum: "))


# Brute Force Approach
print("\nBrute Force Approach")
result = []

def generate(num, subset):

    if num > 9:
        if len(subset) == k and sum(subset) == target:
            result.append(subset.copy())
        return

    # Take
    subset.append(num)
    generate(num + 1, subset)

    # Not Take
    subset.pop()
    generate(num + 1, subset)


generate(1, [])
print(result)

print("Time Complexity: O(2^9 × k)")
print("Space Complexity: O(k)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)
print("\nOptimal Approach")
result = []

def solve(start, target, subset):
    # Valid Combination
    if len(subset) == k:

        if target == 0:
            result.append(subset.copy())
        return

    for i in range(start, 10):
        # Pruning
        if i > target:
            break

        subset.append(i)

        # Next number (Reuse NOT Allowed)
        solve(i + 1, target - i, subset)
        subset.pop()


solve(1, target, [])
print(result)

print("Time Complexity: O(C(9, k))")
print("Space Complexity: O(k)")