n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print()
    
# 1
# 12
# 123
# 1234
# 12345