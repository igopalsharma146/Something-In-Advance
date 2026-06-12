# insertion sort [shifting]
# shifitng right side all the elements that elements are greater than key

arr=[3,4,2,6,4,1,5]
n=len(arr)
for i in range(0,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)
