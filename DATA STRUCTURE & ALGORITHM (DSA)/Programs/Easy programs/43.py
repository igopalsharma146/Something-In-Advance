# Program: Longest Consecutive Sequence

arr = list(map(int, input("Enter array elements separated by space: ").split()))


# Brute Force Approach
longest = 0

for num in arr:
    current = num
    count = 1

    while current + 1 in arr:
        current += 1
        count += 1

    longest = max(longest, count)

print("\nBrute Force Approach")
print("Longest Consecutive Sequence Length:", longest)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
temp = sorted(set(arr))

longest = 1
count = 1

for i in range(1, len(temp)):
    if temp[i] == temp[i - 1] + 1:
        count += 1
    else:
        longest = max(longest, count)
        count = 1

longest = max(longest, count)

print("\nBetter Approach")
print("Longest Consecutive Sequence Length:", longest)
print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")


# Optimal Approach
num_set = set(arr)

longest = 0

for num in num_set:

    if num - 1 not in num_set:

        current = num
        count = 1

        while current + 1 in num_set:
            current += 1
            count += 1

        longest = max(longest, count)

print("\nOptimal Approach")
print("Longest Consecutive Sequence Length:", longest)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")