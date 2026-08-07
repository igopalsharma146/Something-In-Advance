n = int(input("Enter the number of rows: "))

# Upper Part
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

# Lower Part
for i in range(n-1):
    print("*" * (n - i - 1) + " " * (2 * (i+1)) + "*" * (n - i - 1))

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *