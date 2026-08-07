# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     for k in range(2*(n-i-1)):
#         print(" ", end="")
#     for l in range(i+1):
#             print("*", end="")
#     print()

n=int(input("Enter the number of rows: "))
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))



# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************