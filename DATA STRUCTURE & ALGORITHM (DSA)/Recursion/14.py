# Print 1 to N using Tail Recursion

# Tail recursion me direct print(n) karne se output N to 1 aayega. Isliye ek extra parameter use karte hain.
print("\nPrint 1 to N using Tail Recursion :")
def print_1_to_n(i, n):
    if i > n:
        return

    print(i)
    print_1_to_n(i + 1, n)

print_1_to_n(1, 5)

# Print N to 1 using Tail Recursion
print("\nPrint N to 1 using Tail Recursion :")
def print_n_to_1(i, n):
    if i > n:
        return

    print(n)
    print_n_to_1(i, n-1)

print_n_to_1(1, 5)

# Print N to 1 using Tail Recursion
print("\nPrint N to 1 using Tail Recursion :")
def print_n_to_1_(n):
    if n<=0:
        return

    print(n)
    print_n_to_1_(n-1)

print_n_to_1_(5)