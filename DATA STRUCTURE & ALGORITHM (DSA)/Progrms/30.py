# Program: Remove Duplicates from Sorted Array

arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))


# Brute Force Approach
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("\nBrute Force Approach")
print("Array after removing duplicates:", unique)
print("Length:", len(unique))
print("Time Complexity: O(n²)")
print("Space Complexity: O(n)")


# Better Approach
unique = []

for num in arr:
    if len(unique) == 0 or unique[-1] != num:
        unique.append(num)

print("\nBetter Approach")
print("Array after removing duplicates:", unique)
print("Length:", len(unique))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

# Another Better Approach
unique = {}

for num in arr:
    unique[num]=0

print("\nBetter Approach using dict :")
print("Array after removing duplicates:")
j=0
for k,v in unique.items():
    print(k, end=" ")
print("\nLength:", len(unique))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
temp = arr.copy()

i = 0

for j in range(1, len(temp)):
    if temp[j] != temp[i]:
        i += 1
        temp[i] = temp[j]

print("\nOptimal Approach")
print("Array after removing duplicates:", temp[:i + 1])
print("Length:", i + 1)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")