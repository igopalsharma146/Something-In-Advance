#Generate all binary string
# Program: Generate All Binary Strings Without Consecutive 1's

n = int(input("Enter the length of binary string: "))
# Brute Force Approach

print("\nBrute Force Approach")
result = []
for num in range(1 << n):
    binary = ""
    for i in range(n - 1, -1, -1):
        if num & (1 << i):
            binary += "1"
        else:
            binary += "0"

    valid = True
    for i in range(n - 1):
        if binary[i] == '1' and binary[i + 1] == '1':
            valid = False
            break

    if valid:
        result.append(binary)

for binary in result:
    print(binary)

print("Total Valid Strings:", len(result))

print("Time Complexity: O(N × 2^N)")
print("Space Complexity: O(N × 2^N)")


# Better Approach

print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)

print("\nOptimal Approach")
result = []
def generate(index, current):
    if index == n:
        result.append(current)
        return

    # Always place 0
    generate(index + 1, current + "0")

    # Place 1 only if previous character is not 1
    if len(current) == 0 or current[-1] == '0':
        generate(index + 1, current + "1")

generate(0, "")

for binary in result:
    print(binary)

print("Total Valid Strings:", len(result))
print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")