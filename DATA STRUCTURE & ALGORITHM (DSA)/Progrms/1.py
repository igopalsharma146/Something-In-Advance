# Program: Count Number of Digits

num = int(input("Enter a number: "))


# Brute Force Approach
def count_digits_brute(n):
    return len(str(abs(n)))

print("\nBrute Force Approach")
print("Number of digits:", count_digits_brute(num))
print("Time Complexity: O(d)")
print("Space Complexity: O(d)")


# Better Approach
def count_digits_better(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count

print("\nBetter Approach")
print("Number of digits:", count_digits_better(num))
print("Time Complexity: O(d)")
print("Space Complexity: O(1)")


# Optimal Approach
import math

def count_digits_optimal(n):
    n = abs(n)

    if n == 0:
        return 1

    return int(math.log10(n)) + 1

print("\nOptimal Approach")
print("Number of digits:", count_digits_optimal(num))
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")