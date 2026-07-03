# Program: Combination Sum - I

# Combination Sum-I
# ✅ Reuse of same element allowed.
# ✅ Input me distinct elements hote hain.
# ✅ Answer me duplicate combinations nahi honi chahiye.

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter Target Sum: "))


# Brute Force Approach (Generate All Subsequences)
print("\nBrute Force Approach")
result = []
def generate(index, subset):
    if index == len(arr):

        if sum(subset) == target:
            result.append(subset.copy())
        return

    # Take
    subset.append(arr[index])
    generate(index + 1, subset)

    # Not Take
    subset.pop()
    generate(index + 1, subset)


generate(0, [])
print(result)

print("Time Complexity: O(N × 2^N)")
print("Space Complexity: O(N)")


# Better Approach
print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)
print("\nOptimal Approach")
result = []
def solve(index, target, subset):
    # Base Case
    if target == 0:
        result.append(subset.copy())
        return

    if index == len(arr):
        return

    # Take current element (Reuse Allowed)
    if arr[index] <= target:
        subset.append(arr[index])
        solve(index, target - arr[index], subset)
        subset.pop()

    # Not Take current element
    solve(index + 1, target, subset)


solve(0, target, [])
print(result)

print("Time Complexity: Exponential (≈ O(2^Target))")
print("Space Complexity: O(Target)")