n=int(input("Enter the number of rows: "))
for i in range(n):
    val=65
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print(chr(val), end=" ")
        val+=1
    print()
    
#           A 
#         A B C 
#       A B C D E 
#     A B C D E F G 
#   A B C D E F G H I 
# A B C D E F G H I J K 