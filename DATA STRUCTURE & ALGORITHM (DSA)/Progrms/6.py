# Program: Print All Factors and Total Number of Factors

num = int(input("Enter a number: "))


# Brute Force Approach
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("\nBrute Force Approach")
print("Factors:", factors)
print("Total Factors:", len(factors))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach
factors = []

for i in range(1, (num // 2) + 1):
    if num % i == 0:
        factors.append(i)

factors.append(num)

print("\nBetter Approach")
print("Factors:", factors)
print("Total Factors:", len(factors))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
factors = []

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        factors.append(i)

        if i != num // i:
            factors.append(num // i)

factors.sort()

print("\nOptimal Approach")
print("Factors:", factors)
print("Total Factors:", len(factors))
print("Time Complexity: O(√n)")
print("Space Complexity: O(n)")