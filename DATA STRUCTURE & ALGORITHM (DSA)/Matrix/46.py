#Matrix Transpose
nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# n = len(nums)
print("\nMatrix Transpose :")
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
        # print(nums)
print("Original matrix After Transpose:")
for i in range(0,row):
    for j in range(0,col):
        print(nums[i][j],end=' ')
    print()