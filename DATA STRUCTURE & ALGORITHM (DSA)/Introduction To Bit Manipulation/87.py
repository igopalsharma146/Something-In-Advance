# Program: Toggle the ith Bit

# Toggle Definition:
# If bit is 1 → make it 0
# If bit is 0 → make it 1

n = int(input("Enter number: "))
i = int(input("Enter bit position (0-based): "))


# Brute Force Approach

binary = list(bin(n)[2:])

if i >= len(binary):
    binary = ['0'] * (i - len(binary) + 1) + binary

index = len(binary) - 1 - i

if binary[index] == '1':
    binary[index] = '0'
else:
    binary[index] = '1'

result = int("".join(binary), 2)

print("\nBrute Force Approach")
print("Result:", result)

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# Better Approach

temp = n

if ((temp >> i) & 1) == 1:
    result = n - (1 << i)
else:
    result = n + (1 << i)

print("\nBetter Approach")
print("Result:", result)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")


# Optimal Approach

result = n ^ (1 << i)

print("\nOptimal Approach")
print("Result:", result)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")