# combination sum -1 
# we can take any element any time 
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
    solve(index,sum,target,subset)
    
    sum=total
    subset.pop()
    solve(index+1,sum,target,subset)

nums=[2,3,4,5]
result=[]
target=8
solve(0,0,target,[])
print(result)
