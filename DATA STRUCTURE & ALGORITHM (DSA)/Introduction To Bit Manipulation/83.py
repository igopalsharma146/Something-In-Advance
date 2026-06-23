# Program: Swap Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


# Brute Force Approach

x = a
y = b

temp = x
x = y
y = temp

print("\nBrute Force Approach")
print("a =", x)
print("b =", y)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")


# Better Approach

x = a
y = b

x, y = y, x

print("\nBetter Approach")
print("a =", x)
print("b =", y)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")


# Optimal Approach

x = a
y = b

x = x ^ y
y = x ^ y
x = x ^ y

print("\nOptimal Approach")
print("a =", x)
print("b =", y)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")