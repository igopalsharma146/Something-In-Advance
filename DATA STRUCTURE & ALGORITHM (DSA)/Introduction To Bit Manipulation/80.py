# Program: Decimal to Binary Conversion


# Brute Force Approach
num = int(input("Enter a decimal number: "))

binary = ""

if num == 0:
    binary = "0"

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num //= 2

print("\nBrute Force Approach")
print("Binary:", binary)

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# Better Approach
num = int(input("\nEnter a decimal number: "))

binary = []

if num == 0:
    binary.append("0")

while num > 0:
    binary.append(str(num % 2))
    num //= 2

binary.reverse()

print("\nBetter Approach")
print("Binary:", "".join(binary))

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")


# Optimal Approach

num = int(input("\nEnter a decimal number: "))

print("\nOptimal Approach")
print("Binary:", bin(num)[2:]) # it include 0b in starting ex:3 0b0011

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")