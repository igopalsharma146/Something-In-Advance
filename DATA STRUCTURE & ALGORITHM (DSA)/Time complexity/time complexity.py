# Time Complexity is a measure of how the running time of an algorithm grows as the input size n increases.

# It is usually expressed using Big-O notation, which describes the upper bound of an algorithm's growth rate.

# Common time complexities:

# Complexity	Name	Example
# O(1)	Constant	Accessing an array element
# O(logn)	Logarithmic	Binary Search
# O(n)	Linear	Traversing an array
# O(nlogn)	Linearithmic	Merge Sort, Heap Sort
# O(n^2)	Quadratic	Nested loops over the same array
# O(n^3)	Cubic	Triple nested loops
# O(2^n)	Exponential	Recursive Fibonacci (naive)
# O(n!)	Factorial	Generating all permutations
n=9
for i in range(n):
    print(i)

# The loop runs n times, so the time complexity is:

# O(n)