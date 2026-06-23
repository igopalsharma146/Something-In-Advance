# Program: Check if Number is Power of 2

n = int(input("Enter number: "))


# Brute Force Approach

temp = 1

while temp < n:
    temp *= 2

print("\nBrute Force Approach")

if temp == n:
    print("Power of 2")
else:
    print("Not Power of 2")

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Better Approach

count = 0
temp = n

while temp > 0:

    if temp & 1:
        count += 1

    temp >>= 1

print("\nBetter Approach")

if count == 1:
    print("Power of 2")
else:
    print("Not Power of 2")

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

print("\nOptimal Approach")

if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not Power of 2")

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")