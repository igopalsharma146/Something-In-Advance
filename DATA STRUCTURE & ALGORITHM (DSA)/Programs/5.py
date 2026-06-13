# Program: Print All Unique Numbers in a List

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
unique_numbers = []

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        unique_numbers.append(arr[i])

print("\nBrute Force Approach")
print("Unique Numbers:", unique_numbers)
print("Time Complexity: O(n²)")
print("Space Complexity: O(k)")


# Better Approach
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

unique_numbers = []

for num in arr:
    if freq[num] == 1:
        unique_numbers.append(num)

print("\nBetter Approach")
print("Unique Numbers:", unique_numbers)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
xor_result = 0

for num in arr:
    xor_result ^= num

# print("xor result :",xor_result)
rightmost_set_bit = xor_result & -xor_result # -xor_result ka matlab h 2's complement
# print("right most bit :",rightmost_set_bit)

num1 = 0
num2 = 0

for num in arr:
    if num & rightmost_set_bit:
        num1 ^= num
    else:
        num2 ^= num

print("\nOptimal Approach")
print("Unique Numbers:", num1, num2)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")