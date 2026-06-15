# Program: Armstrong Number

num = int(input("Enter a number: "))


# Brute Force Approach
digits = len(str(num))
armstrong_sum = sum(int(digit) ** digits for digit in str(num))

print("\nBrute Force Approach")

if armstrong_sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

print("Time Complexity: O(d)")
print("Space Complexity: O(d)")


# Better Approach
n = num
digits = len(str(num))
armstrong_sum = 0

while n > 0:
    digit = n % 10
    armstrong_sum += digit ** digits
    n //= 10

print("\nBetter Approach")

if armstrong_sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

print("Time Complexity: O(d)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(d)")
print("Space Complexity: O(1)")