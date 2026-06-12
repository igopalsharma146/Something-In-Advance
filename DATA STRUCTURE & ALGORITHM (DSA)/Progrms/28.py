# Program: Find Second Largest Element in an Array

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
sorted_arr = sorted(set(arr))

print("\nBrute Force Approach")

if len(sorted_arr) < 2:
    print("Second Largest Element does not exist")
else:
    print("Second Largest Element:", sorted_arr[-2])

print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")


# Better Approach
largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num>largest:
        largest=num

for num in arr:
    if num != largest and num > second_largest:
        second_largest = num

print("\nBetter Approach")

if second_largest == float('-inf'):
    print("Second Largest Element does not exist")
else:
    print("Second Largest Element:", second_largest)

print("Time Complexity: O(2n)")
print("Space Complexity: O(1)")


# Optimal Approach
largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("\nOptimal Approach")

if second_largest == float('-inf'):
    print("Second Largest Element does not exist")
else:
    print("Second Largest Element:", second_largest)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")