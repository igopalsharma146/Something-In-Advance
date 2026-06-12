def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


arr = [3, 6, 5, 2, 8, 5, 67, 35, 3, 5, 67, 33]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

#working: hame pivot array ke last element ko lena h , agar j ke loop me pivot se chhota element milta h to i+=1 karke arr[i] se arr[j] ko swap kar denge.

# Quick Sort Partition (Lomuto Partition) Working
# 1. Pivot ko array ke last element (arr[high]) ke roop me choose karte hain.
# 2. i = low - 1 rakhte hain.
# i us position ko represent karta hai jahan tak pivot se chhote elements rakhe gaye hain.
# 3. j ko low se high-1 tak chalate hain.

# 4. Har iteration me check karte hain:

#   if arr[j] < pivot:

# Agar element pivot se chhota hai:

#   i += 1
#   arr[i] aur arr[j] ko swap kar do.

# Isse pivot se chhote elements array ke left side me collect hote rehte hain.

# 5. Agar arr[j] >= pivot hai to kuch nahi karna, sirf next iteration par chale jana.
# 6. Loop khatam hone ke baad:
# 0 se i tak ke sab elements pivot se chhote honge.
# i+1 se high-1 tak ke elements pivot se bade ya equal honge.
# Pivot abhi bhi last position par hoga.
# 7. Ab pivot ko uski correct position par lane ke liye:
#     arr[i+1], arr[high] = arr[high], arr[i+1]

# swap kar dete hain.

# 8. i+1 pivot ka final index ban jata hai, isliye:

# return i+1
# 9. Ab:
# Pivot ke left me saare elements chhote hain.
# Pivot ke right me saare elements bade ya equal hain.

# 10. Quick Sort recursively:

# Left part (low se pivot_index-1)
# Right part (pivot_index+1 se high)

# ko sort karta hai.




#Agar ham starting element ko pivot lete h to
def partition(arr, low, high):
    pivot = arr[low]

    i = low + 1
    j = high

    while True:

        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j