n=int(input("Enter the number of rows: "))
for i in range(n):
    val=65
    for j in range(n-i):
        print(chr(val), end=" ")
        val+=1
    print()

# A B C D E F G 
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 