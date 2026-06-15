# Program: Left Rotate Array by K Places

arr = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter value of k: "))

n = len(arr)

if n == 0:
    print("Array is empty")
else:

    k = k % n


    # Brute Force Approach
    temp = arr.copy()

    for _ in range(k):
        first = temp[0]

        for i in range(n - 1):
            temp[i] = temp[i + 1]

        temp[n - 1] = first

    print("\nBrute Force Approach")
    print("Array after left rotation:", temp)
    print("Time Complexity: O(n*k)")
    print("Space Complexity: O(1)")


    # Better Approach
    temp = arr[k:] + arr[:k]

    print("\nBetter Approach")
    print("Array after left rotation:", temp)
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")


    # Optimal Approach

    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    temp = arr.copy()

    reverse(temp, 0, k - 1)      # Reverse first k elements
    reverse(temp, k, n - 1)      # Reverse remaining elements
    reverse(temp, 0, n - 1)      # Reverse complete array

    print("\nOptimal Approach")
    print("Array after left rotation:", temp)
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")