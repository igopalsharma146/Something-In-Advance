# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     for k in range(2*i):
#         print(" ", end="")
#     for l in range(n-i):
#             print("*", end="")
#     print()

n=int(input("Enter the number of rows: "))
for i in range(n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))


# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *