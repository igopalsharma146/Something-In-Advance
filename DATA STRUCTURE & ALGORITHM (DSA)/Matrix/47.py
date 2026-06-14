#Set matrix zeros

def set_zeros(matrix,row,col):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(0,r):
        if matrix[i][col]!=0:
            matrix[i][col]=float("inf")
    for j in range(0,c):
        if matrix[row][j]!=0:
            matrix[row][j]=float("inf")

nums = [[1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]]
temp = [row[:] for row in nums]


row=len(nums)
col=len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if nums[i][j]==0:
            set_zeros(nums,i,j)

for i in range(0,row):
    for j in range(0,col):
        if nums[i][j]==float("inf"):
            nums[i][j]=0

print("Original matrix After set zeros:")
for i in range(0,row):
    for j in range(0,col):
        print(nums[i][j],end=' ')
    print()
print("Time complexity : O(r x c) + O(k x (r + c)) + O(r x c)")

# Better Approach
# temp = [row[:] for row in nums]
row = len(temp)
col = len(temp[0])

rows = [0] * row
cols = [0] * col

for i in range(row):
    for j in range(col):

        if temp[i][j] == 0:
            rows[i] = 1
            cols[j] = 1

for i in range(row):
    for j in range(col):

        if rows[i] == 1 or cols[j] == 1:
            temp[i][j] = 0

print("\nBetter Approach")
for r in temp:
    print(r)

print("Time Complexity: O(m*n)")
print("Space Complexity: O(m+n)")