# Program: Rearrange Array Elements by Sign

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
positive = []
negative = []

for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

result = []
i = 0

while i < len(positive) and i < len(negative):
    result.append(positive[i])
    result.append(negative[i])
    i += 1

while i < len(positive):
    result.append(positive[i])
    i += 1

while i < len(negative):
    result.append(negative[i])
    i += 1

print("\nBrute Force Approach")
print("Rearranged Array:", result)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach
positive = []
negative = []

for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

result = [0] * len(arr)

pos_idx = 0
neg_idx = 1

for num in positive:
    if pos_idx < len(arr):
        result[pos_idx] = num
        pos_idx += 2

for num in negative:
    if neg_idx < len(arr):
        result[neg_idx] = num
        neg_idx += 2

print("\nBetter Approach")
print("Rearranged Array:", result)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")