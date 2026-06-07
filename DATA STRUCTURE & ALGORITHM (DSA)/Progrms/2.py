# Program: Reverse a Number

num = int(input("Enter a number: "))


# Brute Force Approach
reversed_num = int(str(abs(num))[::-1])

if num < 0:
    reversed_num = -reversed_num

print("\nBrute Force Approach")
print("Reversed Number:", reversed_num)
print("Time Complexity: O(d)")
print("Space Complexity: O(d)")


# Better Approach
n = abs(num)
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

if num < 0:
    reversed_num = -reversed_num

print("\nBetter Approach")
print("Reversed Number:", reversed_num)
print("Time Complexity: O(d)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(d)")
print("Space Complexity: O(1)")