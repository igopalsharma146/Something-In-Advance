# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0 and j%2==0:
#             print("1", end="")
#         elif i%2!=0 and j%2!=0:
#             print("1", end="")
#         else:
#             print("0", end="")
#     print()

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

# 1
# 01
# 101
# 0101
# 10101
# 010101
# 1010101