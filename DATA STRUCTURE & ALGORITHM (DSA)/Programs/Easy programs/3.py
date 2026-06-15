# Program: Check Palindrome Number

num = int(input("Enter a number: "))


# Brute Force Approach
is_palindrome = str(num) == str(num)[::-1]

print("\nBrute Force Approach")

if is_palindrome:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

print("Time Complexity: O(d)")
print("Space Complexity: O(d)")


# Better Approach
n = abs(num)
original = n
reverse_num = 0

while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n //= 10

print("\nBetter Approach")

if original == reverse_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

print("Time Complexity: O(d)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(d)")
print("Space Complexity: O(1)")