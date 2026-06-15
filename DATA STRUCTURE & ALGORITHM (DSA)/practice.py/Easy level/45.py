nums=[[1,2,3],[4,5,6],[7,8,9]]
# print upper trinangle
#print lower triangle
#print both diagonal

#upper triangle
print("upper triangle :")
row=len(nums)
col=len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if j>=i:
            print(nums[i][j],end=' ')
        else:
            print("*",end=' ')
    print()
    
#Lower triangle
print("Lower triangle :")
row=len(nums)
col=len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if j<=i:
            print(nums[i][j],end=' ')
        else:
            print("*",end=' ')
    print()
    
#Diagonal 
print("Diagonal :")
row=len(nums)
col=len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if j==i:
            print(nums[i][j],end=' ')
        else:
            print("*",end=' ')
    print()
    
#Diagonal 
print("Another Diagonal :")
row=len(nums)
col=len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if j+i==row-1:
            print(nums[i][j],end=' ')
        else:
            print("*",end=' ')
    print()
    
#Matrix Transpose
print("Matrix Transpose :")
row=len(nums)
col=len(nums[0])
print("Original matrix :")
for i in range(0,row):
    for j in range(0,col):
        print(nums[i][j],end=' ')
    print()
print("\nMatrix Transpose")
for i in range(0,row):
    for j in range(i+1,col):
        nums[j][i],nums[i][j]=nums[i][j],nums[j][i]
        print(nums)
print("Original matrix :")
for i in range(0,row):
    for j in range(0,col):
        print(nums[i][j],end=' ')
    print()