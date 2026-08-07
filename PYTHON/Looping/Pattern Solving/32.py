n = int(input("Enter the number of rows: "))
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        distance = min(i, j, size - 1 - i, size - 1 - j)
        print(n - distance, end="")
    print()
    
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444