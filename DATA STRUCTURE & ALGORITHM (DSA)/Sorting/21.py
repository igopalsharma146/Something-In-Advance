# Selection sort
arr=[9,8,7,6,5,4,3,3,2,5]
n=len(arr)
for i in range(0,n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
    
print(arr)

# # Selection sort
# arr=[9,8,7,6,5,4,3,3,2,5]
# n=len(arr)
# for i in range(0,n):
#     min=arr[i]
#     for j in range(i+1,n):
#         if arr[j]<min:
#             min=arr[j]
#     arr[i],min=min,arr[i] #yaha per actual value change nhi ho rahi sirf min ki value change ho rahi hai
#     print(arr)
# print(arr)