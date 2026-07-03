# Program: Combination Sum - II

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter Target Sum: "))
arr.sort()


# Brute Force Approach (Generate All Subsequences)

print("\nBrute Force Approach")
result = []

def generate(index, subset):
    if index == len(arr):
        if sum(subset) == target and subset not in result:
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

    for i in range(index, len(arr)):
        # Skip Duplicates
        if i > index and arr[i] == arr[i - 1]:
            continue

        # Pruning
        if arr[i] > target:
            break
        subset.append(arr[i])

        # Move to next index (Element can be used only once)
        solve(i + 1, target - arr[i], subset)
        subset.pop()


solve(0, target, [])
print(result)

print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")