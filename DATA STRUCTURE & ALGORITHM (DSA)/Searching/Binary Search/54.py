# Program: Lower Bound

# Lower Bound
# Definition:First index jahan value >= target ho

# Upper Bound
# Definition:First index jahan value > target ho

def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1
    return ans


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
print("Lower Bound Index:", lower_bound(arr, target))
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")



# Program: Upper Bound
# Upper Bound
# Definition:First index jahan value > target ho

def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1
    return ans


# arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
print("Upper Bound Index:", upper_bound(arr, target))
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")