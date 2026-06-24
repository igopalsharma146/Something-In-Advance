# Program: Print All Subsequences
arr = list(map(int, input("Enter array elements: ").split()))


# Brute Force Approach (Bit Manipulation)

n = len(arr)
print("\nBrute Force Approach")
for mask in range(1 << n):
    # print("mask :",mask)
    subsequence = []

    for i in range(n):

        if mask & (1 << i):
            # print("mask & (1 << i) :",mask & (1 << i))
            subsequence.append(arr[i])

    print(subsequence)

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(N)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Recursion / Backtracking)

print("\nOptimal Approach")

def print_subsequences(index, current):

    if index == len(arr):
        print(current)
        return

    # Take current element
    current.append(arr[index])
    print_subsequences(index + 1, current)

    # Don't take current element
    current.pop()
    print_subsequences(index + 1, current)


print_subsequences(0, [])

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(N)")


        #          []
        #        /    \
        #      1       Not 1
        #    /  \      /   \
        #   2   N2    2    N2
        #  / \        / \
        # 3  N3      3  N3