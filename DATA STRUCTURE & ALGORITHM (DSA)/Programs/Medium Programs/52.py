# Program: 4 Sum

arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target sum: "))


# Brute Force Approach
result = set()

n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):

                if arr[i] + arr[j] + arr[k] + arr[l] == target:
                    temp = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                    result.add(temp)

print("\nBrute Force Approach")
print("Quadruplets:", list(result))
print("Time Complexity: O(n⁴)")
print("Space Complexity: O(k)")


# Better Approach
result = set()

for i in range(n):
    for j in range(i + 1, n):

        seen = set()

        for k in range(j + 1, n):

            fourth = target - (arr[i] + arr[j] + arr[k])

            if fourth in seen:
                temp = tuple(sorted([arr[i], arr[j], arr[k], fourth]))
                result.add(temp)

            seen.add(arr[k])

print("\nBetter Approach")
print("Quadruplets:", list(result))
print("Time Complexity: O(n³)")
print("Space Complexity: O(n)")


# Optimal Approach
arr.sort()

result = []

for i in range(n):

    if i > 0 and arr[i] == arr[i - 1]:
        continue

    for j in range(i + 1, n):

        if j > i + 1 and arr[j] == arr[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:

            total = arr[i] + arr[j] + arr[left] + arr[right]

            if total < target:
                left += 1

            elif total > target:
                right -= 1

            else:

                result.append(
                    [arr[i], arr[j], arr[left], arr[right]]
                )

                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

print("\nOptimal Approach")
print("Quadruplets:", result)
print("Time Complexity: O(n³)")
print("Space Complexity: O(1)")