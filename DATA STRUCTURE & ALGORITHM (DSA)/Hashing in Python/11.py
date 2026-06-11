# Program: Count Frequency of Characters of m Array from String n

n = "saudfiusjdbfdfshbakj"
m = ["a", "f", "g", "e", "c"]


# Brute Force Approach
print("\nBrute Force Approach")

for ch in m:
    count = 0

    for char in n:
        if ch == char:
            count += 1

    print(f"{ch} -> {count}")

print("Time Complexity: O(n*m)")
print("Space Complexity: O(1)")


# Better Approach
print("\nBetter Approach")

freq = {}

for char in n:
    freq[char] = freq.get(char, 0) + 1

for ch in m:
    print(f"{ch} -> {freq.get(ch, 0)}")

print("Time Complexity: O(n + m)")
print("Space Complexity: O(k)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n + m)")
print("Space Complexity: O(k)")