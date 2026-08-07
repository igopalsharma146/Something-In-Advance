# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     val=65
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print(chr(val), end=" ")
#         val+=1
#     val=65
#     for k in range(i):
#             print(chr(val), end=" ")
#             val+=1
#     print()


n = int(input("Enter the number of rows: "))
for i in range(n):
    # Spaces
    print("  " * (n - i - 1), end="")

    # First half
    for j in range(i + 1):
        print(chr(65 + j), end=" ")

    # Second half
    for j in range(i):
        print(chr(65 + j), end=" ")

    print()
    
    
#             A 
#           A B A 
#         A B C A B 
#       A B C D A B C 
#     A B C D E A B C D 
#   A B C D E F A B C D E 
# A B C D E F G A B C D E F 