n=int(input("Enter the number of rows: "))
val=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+val), end=" ")
        val+=1
    print()

# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# P Q R S T U 
# V W X Y Z [ \ 