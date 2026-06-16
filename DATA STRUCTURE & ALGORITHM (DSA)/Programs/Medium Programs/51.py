# Program: 3 Sum

# arr = list(map(int, input("Enter array elements separated by space: ").split()))
arr = [1,2,0,-1,2,-2,3,1,-4,0,-1]

# Brute Force Approach
result = set()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):

            if arr[i] + arr[j] + arr[k] == 0:
                temp = tuple(sorted([arr[i], arr[j], arr[k]]))
                result.add(temp)

print("\nBrute Force Approach")
print("Triplets:", list(result))
print("Time Complexity: O(n³)")
print("Space Complexity: O(k)")


# Better Approach
result = set()

for i in range(len(arr)):

    seen = set()

    for j in range(i + 1, len(arr)):

        third = -(arr[i] + arr[j])

        if third in seen:
            temp = tuple(sorted([arr[i], arr[j], third]))
            result.add(temp)

        seen.add(arr[j])

print("\nBetter Approach")
print("Triplets:", list(result))
print("Time Complexity: O(n²)")
print("Space Complexity: O(n)")


# Optimal Approach
arr.sort()

result = []

for i in range(len(arr)):

    if i > 0 and arr[i] == arr[i - 1]:
        continue

    left = i + 1
    right = len(arr) - 1

    while left < right:

        total = arr[i] + arr[left] + arr[right]

        if total < 0:
            left += 1

        elif total > 0:
            right -= 1

        else:

            result.append([arr[i], arr[left], arr[right]])

            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

print("\nOptimal Approach")
print("Triplets:", result)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")