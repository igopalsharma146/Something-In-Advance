# 1. Parameterized Recursion

# Jab answer/function ka state parameters me carry kiya jata hai, use Parameterized Recursion kehte hain.

# Example: Sum of first N numbers
print("\nSum of first N numbers using Parameterized Recursion :")
def sum_n(n, total):
    if n == 0:
        print(total)
        return

    sum_n(n - 1, total + n)

sum_n(5, 0)

# 2. Functional Recursion
# Jab recursive call kuch return kare aur function us returned value ka use kare, use Functional Recursion kehte hain.

# Example: Sum of first N numbers
print("\nSum of first N numbers using Functional Recursion :")
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))