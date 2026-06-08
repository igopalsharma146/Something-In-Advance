# Program: Find Unique Number in Array

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
unique = -1

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        unique = arr[i]
        break

print("\nBrute Force Approach")
print("Unique Number:", unique)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

unique = -1

for num in arr:
    if freq[num] == 1:
        unique = num
        break

print("\nBetter Approach")
print("Unique Number:", unique)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
unique = 0

for num in arr:
    unique ^= num

print("\nOptimal Approach")
print("Unique Number:", unique)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")