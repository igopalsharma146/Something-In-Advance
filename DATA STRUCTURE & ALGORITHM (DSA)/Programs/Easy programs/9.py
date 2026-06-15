# Program: Find the Extra Number in Two Arrays

arr1 = list(map(int, input("Enter first array elements separated by space: ").split()))
arr2 = list(map(int, input("Enter second array elements separated by space: ").split()))


# Brute Force Approach
extra = -1

for num in arr2:
    temp = arr1.copy()

    if num in temp:
        temp.remove(num)
    else:
        extra = num
        break

print("\nBrute Force Approach")
print("Extra Number:", extra)
print("Time Complexity: O(n²)")
print("Space Complexity: O(n)")


# Better Approach
freq = {}

for num in arr1:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

extra = -1

for num in arr2:
    if num in freq and freq[num] > 0:
        freq[num] -= 1
    else:
        extra = num
        break

print("\nBetter Approach")
print("Extra Number:", extra)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
xor_result = 0

for num in arr1:
    xor_result ^= num

for num in arr2:
    xor_result ^= num

print("\nOptimal Approach")
print("Extra Number:", xor_result)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
