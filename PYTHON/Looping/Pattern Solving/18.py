n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    for k in range(n*2-2*i-2):
        print(" ", end="")
    for j in range(i+1,0,-1):
        print(j, end="")
    print()
    
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321