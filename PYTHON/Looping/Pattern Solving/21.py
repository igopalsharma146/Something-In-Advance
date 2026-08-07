n=int(input("Enter the number of rows: "))
for i in range(n):
    val=65
    for j in range(i+1):
        print(chr(val), end=" ")
        val+=1
    print()
    
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F 
# A B C D E F G