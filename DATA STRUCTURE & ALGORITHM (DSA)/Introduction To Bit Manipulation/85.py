# Program: Set the ith Bit

n = int(input("Enter number: "))
i = int(input("Enter bit position (0-based): "))


# Brute Force Approach

binary = list(bin(n)[2:])

if i >= len(binary):
    binary = ['0'] * (i - len(binary) + 1) + binary

binary[len(binary) - 1 - i] = '1'

result = int("".join(binary), 2)

print("\nBrute Force Approach")
print("Result:", result)

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# Better Approach

result = n

if ((n >> i) & 1) == 0:
    result = n + (1 << i)

print("\nBetter Approach")
print("Result:", result)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")


# Optimal Approach

result = n | (1 << i)

print("\nOptimal Approach")
print("Result:", result)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")