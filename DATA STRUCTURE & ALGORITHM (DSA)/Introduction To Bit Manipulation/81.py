# Program: Binary to Decimal Conversion


# Brute Force Approach
binary = input("Enter a binary number: ")

decimal = 0
power = 0

for i in range(len(binary) - 1, -1, -1):
    decimal += int(binary[i]) * (2 ** power)
    power += 1

print("\nBrute Force Approach")
print("Decimal:", decimal)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
binary = input("\nEnter a binary number: ")

decimal = 0

for bit in binary:
    decimal = decimal * 2 + int(bit)

print("\nBetter Approach")
print("Decimal:", decimal)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Optimal Approach

binary = input("\nEnter a binary number: ")

print("\nOptimal Approach")
print("Decimal:", int(binary, 2))

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")