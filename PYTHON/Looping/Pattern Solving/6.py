n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()

# 12345
# 1234
# 123
# 12
# 1