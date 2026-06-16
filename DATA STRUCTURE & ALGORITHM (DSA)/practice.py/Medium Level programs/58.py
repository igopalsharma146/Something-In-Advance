# occurence of a number
arr=[1,2,2,3,3,4,4,5,5,5,6,7,7,7]
target=int(input("Enter a number:"))
n=len(arr)
lb=-1
ub=n
left,right=0,n-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]>=target:
        lb=mid
        right=mid-1
    else:
        left=mid+1
# print(lb)
if lb==-1:
    print(f"Element is not present.")

ub=n
left,right=0,n-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]>target:
        ub=mid
        right=mid-1
    else:
        left=mid+1
print(f"Occurence {ub-lb}")
# print(ub)
