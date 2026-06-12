# Quick Sort (Recursion)

# Quick Sort me ek element ko pivot mante hain, phir array ko do parts me divide karte hain:

# Pivot se chhote elements left me
# Pivot se bade elements right me

# Uske baad left aur right part par recursively Quick Sort lagate hain.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    
    left = [x for x in arr[1:] if x <= pivot]
    print(left)
    right = [x for x in arr[1:] if x > pivot]
    print(right)

    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [3, 6, 5, 2, 8, 5, 67, 35, 3, 5, 67, 33]

print(quick_sort(nums))