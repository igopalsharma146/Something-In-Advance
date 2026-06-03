# Getrefcount Anomaly
import sys
a = []
print(sys.getrefcount(a))  # Output: 2
b = a
print(sys.getrefcount(a))  # Output: 3

# Explanation: The reference count of a list in Python includes the reference from the variable itself and the reference from the list's internal structure. When you create a new variable b and assign it to the same list a, the reference count increases by one.

a=2
print(sys.getrefcount(a))  # Output: 2

a=256
print(sys.getrefcount(a))  # Output: 2

a=257
print(sys.getrefcount(a))  # Output: 2