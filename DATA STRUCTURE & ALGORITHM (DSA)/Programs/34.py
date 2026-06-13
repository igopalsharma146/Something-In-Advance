# Program: Move Zeros to End of the List

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
temp = []

for num in arr:
    if num != 0:
        temp.append(num)

zero_count = len(arr) - len(temp)

for _ in range(zero_count):
    temp.append(0)

print("\nBrute Force Approach")
print("Array after moving zeros to end:", temp)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach
temp = arr.copy()

for i in range(len(temp)):
    if temp[i] == 0:

        for j in range(i + 1, len(temp)):
            if temp[j] != 0:
                temp[i], temp[j] = temp[j], temp[i]
                break

print("\nBetter Approach")
print("Array after moving zeros to end:", temp)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Optimal Approach
temp = arr.copy()

j = -1

for i in range(len(temp)):
    if temp[i] == 0:
        j = i
        break

if j != -1:
    for i in range(j + 1, len(temp)):
        if temp[i] != 0:
            temp[i], temp[j] = temp[j], temp[i]
            j += 1

print("\nOptimal Approach")
print("Array after moving zeros to end:", temp)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")