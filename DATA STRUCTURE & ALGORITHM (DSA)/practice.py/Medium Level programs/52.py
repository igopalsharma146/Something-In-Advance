# 4 sum
arr=[1,-2,-1,2,0,-1,0,1,3]
target=int(input("Enter the number :"))

# brute force 
result=set()
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if arr[i]+arr[j]+arr[k]+arr[l]==target:
                    temp=tuple(sorted([arr[i],arr[j],arr[k],arr[l]]))
                    result.add(temp)
print(result)

#better solution
result=set()
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        my_set=set()
        for k in range(j+1,n):
            fourth=target-(arr[i]+arr[j]+arr[k])
            if fourth in my_set:
                temp=tuple(sorted([arr[i],arr[j],arr[k],fourth]))
                result.add(temp)
            
            my_set.add(arr[k])
print(result)

#optimal solution
arr.sort()
# print(arr)
# print(target)
# target=0
result=set()
n=len(arr)
for i in range(n):
    if i>0 and arr[i]==arr[i-1]:
        continue

    for j in range(i+1,n):
        if j>i+1 and arr[j]==arr[j-1]:
            continue

        left=j+1
        right=n-1
        while left<right:
            
            current_sum=arr[i]+arr[j]+arr[left]+arr[right]
            if current_sum<target:
                left+=1
            elif current_sum>target:
                right-=1
            else:
                # print("Found:", arr[i], arr[j], arr[left], arr[right])
                result.add((arr[i],arr[j],arr[left],arr[right]))
                left+=1
                right-=1
            
                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
print(result)