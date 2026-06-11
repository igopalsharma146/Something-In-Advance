# Print 1 to N using Head Recursion
print("\nPrint 1 to N using HEAD Recursion :")
def print_1_to_n(n):
    if n == 0:
        return

    print_1_to_n(n - 1)
    print(n)

print_1_to_n(5)

# Print N to 1 using HEAD Recursion
print("\nPrint N to 1 using HEAD Recursion :")
def print_n_to_1(i, n):
    if i > n:
        return

    print_n_to_1(i+1, n)
    print(i)

print_n_to_1(1, 5)