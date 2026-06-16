# search in rotated sorted array where duplicate value not in array
arr=[8,9,10,1,2,3,4,5,6,7]
target=int(input("Enter the element :"))
n=len(arr)
left,right=0,n-1
while left <= right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(mid)
        break
    if arr[mid]<=arr[right]:
        if arr[mid]<=target<=arr[right]:
            left=mid+1
        else:
            right=mid-1
    else:
        if arr[left]<=target<=arr[mid]:
            right=mid-1
        else:
            left=mid+1
