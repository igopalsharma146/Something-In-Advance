# Introduction to Bit Manipulation
# Bit Manipulation ka matlab hai numbers ke binary representation par operations karna.
# Example:
# Decimal 5 = 101
# Decimal 3 = 011
# Hum in bits par directly kaam karte hain.

# Why Learn Bit Manipulation?
# Kai problems jo normally:
# O(n)
# me solve hoti hain, unhe bit manipulation se:
# O(1)
# ya
# O(log n)
# me solve kar sakte hain.

# Interview me bahut use hota hai:
# Check Odd/Even
# Power of 2
# Count Set Bits
# Unique Number
# XOR Problems
# Subsets
# Bit Masking

# Bitwise Operators

# 1. AND (&)
# Rule:
# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

# Example:
a = 5
b = 3
print(a & b)

# Binary:
# 5 = 101
# 3 = 011
# ---------
#     001

# 2. OR (|)
# Rule:
# 1 | 1 = 1
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0

# Example:
print(5 | 3)
# 101
# 011
# ---
# 111

# 3. XOR (^)
# Rule:
# 1 ^ 1 = 0
# 0 ^ 0 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1

# Example:
print(5 ^ 3)
# 101
# 011
# ---
# 110

# Important XOR Properties
a ^ a = 0
a ^ 0 = a
a ^ b ^ a = b

# 4. NOT (~)
# Example:
print(~5)
# Output:
# -6

# Reason:
# ~n = -(n+1)
# ~5 = -(5+1)
# = -6

# Shift Operators

# 1. Left Shift (<<)
print(5 << 1)
# Binary:
# 5 = 0101
# 0101 << 1
# 1010

# Formula:
    # n << k
    # = n * (2^k)
    # Example:
    # 5 << 2
    # = 5 * 4
    # = 20
    
# 2. Right Shift (>>)
print(20 >> 2)
# Binary:
# 20 = 10100
# 10100 >> 2
# 00101

# Formula:
    # n >> k
    # = n // (2^k)