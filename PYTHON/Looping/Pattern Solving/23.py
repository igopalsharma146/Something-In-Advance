n=int(input("Enter the number of rows: "))
val=65
for i in range(n):
    for j in range(i+1):
        print(chr(val), end=" ")
    val+=1
    print()

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 