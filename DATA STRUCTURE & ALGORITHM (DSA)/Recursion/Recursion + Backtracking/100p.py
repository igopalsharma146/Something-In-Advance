# combination sum-2
# pick 1 element at a time
# no duplicate
def solve(index,total,target,subset):
    #base condition
    if total==target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if index>=len(nums):
        return
    
    sum=total+nums[index]
    subset.append(nums[index])
    solve(index+1,sum,target,subset)
    
    sum=total
    subset.pop()
    solve(index+1,sum,target,subset)

nums=[1,1,2,1,2]
result=[]
target=4
solve(0,0,target,[])
print(result)
