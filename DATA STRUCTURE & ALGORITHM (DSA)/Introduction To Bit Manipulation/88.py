# Program: Remove the Rightmost Set Bit

n = int(input("Enter number: "))


# Brute Force Approach

binary = list(bin(n)[2:])

for i in range(len(binary) - 1, -1, -1):

    if binary[i] == '1':
        binary[i] = '0'
        break

result = int("".join(binary), 2)

print("\nBrute Force Approach")
print("Result:", result)

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# Better Approach

temp = n
pos = 0

while temp:

    if temp & 1:
        break

    pos += 1
    temp >>= 1

result = n & ~(1 << pos)

print("\nBetter Approach")
print("Result:", result)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

result = n & (n - 1)

print("\nOptimal Approach")
print("Result:", result)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")