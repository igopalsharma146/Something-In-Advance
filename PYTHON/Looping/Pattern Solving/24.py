n=int(input("Enter the number of rows: "))
for i in range(n):
    val=64+n
    for j in range(i+1):
        print(chr(val), end=" ")
        val-=1
    print()

# G 
# G F 
# G F E 
# G F E D 
# G F E D C 
# G F E D C B 
# G F E D C B A 