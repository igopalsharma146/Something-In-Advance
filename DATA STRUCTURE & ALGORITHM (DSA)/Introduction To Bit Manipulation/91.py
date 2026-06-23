# Program: Find Single Number in Array

arr = list(map(int, input("Enter array elements: ").split()))

# Brute Force Approach
single = -1
for i in range(len(arr)):
    count = 0
    
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        single = arr[i]
        break

print("\nBrute Force Approach")
print("Single Number:", single)

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")


# Better Approach

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

single = -1
for key, value in freq.items():
    if value == 1:
        single = key
        break

print("\nBetter Approach")
print("Single Number:", single)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")


# Optimal Approach
single = 0
for num in arr:
    single ^= num

print("\nOptimal Approach")
print("Single Number:", single)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")