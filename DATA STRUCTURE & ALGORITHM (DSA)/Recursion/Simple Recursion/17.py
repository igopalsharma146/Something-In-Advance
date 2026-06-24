#reverse an array
def reverse_an_array(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
    return reverse_an_array(arr,left,right)
arr=[2,5,4,3,6]
reverse_an_array(arr,0,4)
print(arr)