# merge sort [devide and merge]

#merging two sorted array
def merge_array(arr1,arr2):
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
    return result


#deviding array
nums=[3,6,5,2,8,5,67,35,3,5,67,33]
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid=len(arr)//2
    left_array=arr[:mid]
    right_array=arr[mid:]
    left=merge_sort(left_array)
    right=merge_sort(right_array)
    return merge_array(left,right)

res=merge_sort(nums)
print(res)