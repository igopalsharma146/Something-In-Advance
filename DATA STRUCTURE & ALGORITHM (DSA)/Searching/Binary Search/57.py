# Program: Find First and Last Occurrence

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))


# Brute Force Approach
first = -1
last = -1

for i in range(len(arr)):

    if arr[i] == target:

        if first == -1:
            first = i

        last = i

print("\nBrute Force Approach")
print("First Occurrence:", first)
print("Last Occurrence :", last)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Better Approach
first = -1
last = -1

# First Occurrence
left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        first = mid
        right = mid - 1

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


# Last Occurrence
left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        last = mid
        left = mid + 1 #difference

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print("\nBetter Approach")
print("First Occurrence:", first)
print("Last Occurrence :", last)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Optimal Approach

def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


first = first_occurrence(arr, target)
last = last_occurrence(arr, target)

print("\nOptimal Approach")
print("First Occurrence:", first)
print("Last Occurrence :", last)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


#esko hum lower bound or upper bound ki help se bhi nikal sakte hai
def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


def upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


lb = lower_bound(arr, target)

if lb == len(arr) or arr[lb] != target:
    first = -1
    last = -1
else:
    first = lb
    last = upper_bound(arr, target) - 1