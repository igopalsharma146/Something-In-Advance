# Program: Power Set (Print All Subsets)
arr = list(map(int, input("Enter array elements: ").split()))


# Brute Force Approach

n = len(arr)
subsets = []

for mask in range(2 ** n):
    subset = []

    for i in range(n):
        if mask & (1 << i):
            subset.append(arr[i])

    subsets.append(subset)

print("\nBrute Force Approach")
print("All Subsets:")

for subset in subsets:
    print(subset)
print("Total Subsets:", len(subsets))
print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(N * 2^N)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)

result = []
def generate_subset(index, current):
    if index == len(arr):
        result.append(current[:])
        return

    # Include current element
    current.append(arr[index])
    generate_subset(index + 1, current)

    # Exclude current element
    current.pop()
    generate_subset(index + 1, current)


generate_subset(0, [])
print("\nOptimal Approach")
print("All Subsets:")

for subset in result:
    print(subset)

print("Total Subsets:", len(result))

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(N)")