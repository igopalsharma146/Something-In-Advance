#merging two sorted array
arr1=[3,4,6,7,8,22,45,65,67]
arr2=[1,2,4,7,9,22,56,65,66,67,78]

result=[]
l1=len(arr1)
l2=len(arr2)
i,j=0,0
while i<l1 and j<l2:
    if arr1[i]<arr2[j]:
        result.append(arr1[i])
        i+=1
    else:
        result.append(arr2[j])
        j+=1
if i<l1:
    while i<l1:
        result.append(arr1[i])
        i+=1
if j<l2:
    while j<l2:
        result.append(arr2[j])
        j+=1
print(result)