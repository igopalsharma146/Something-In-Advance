# Program: Check if the ith Bit is Set or Not

n = int(input("Enter number: "))
i = int(input("Enter bit position (0-based): "))


# Brute Force Approach

binary = bin(n)[2:]

if i >= len(binary):
    result = False
else:
    result = binary[len(binary) - 1 - i] == '1'

print("\nBrute Force Approach")
print("Set Bit" if result else "Not Set Bit")

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# Better Approach

temp = n

for _ in range(i):
    temp = temp >> 1

result = temp & 1

print("\nBetter Approach")
print("Set Bit" if result else "Not Set Bit")

print("Time Complexity: O(i)")
print("Space Complexity: O(1)")

# Another Better Approach
print("\nAnother Better solution")
temp1=n
if ((temp1>>i)&1)==1:
    print("True")
else:
    print("False")
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

# Optimal Approach
result = n & (1 << i)

print("\nOptimal Approach")
print("Set Bit" if result else "Not Set Bit")

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")