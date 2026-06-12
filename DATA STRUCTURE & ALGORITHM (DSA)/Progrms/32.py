# Program: Right Rotate Array by K Places

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
        last = temp[-1]

        for i in range(len(temp) - 1, 0, -1):
            temp[i] = temp[i - 1]

        temp[0] = last

    print("\nBrute Force Approach")
    print("Array after right rotation:", temp)
    print("Time Complexity: O(n*k)")
    print("Space Complexity: O(1)")


    # Better Approach
    temp = arr[n - k:]

    for i in range(n - k):
        temp.append(arr[i])

    print("\nBetter Approach")
    print("Array after right rotation:", temp)
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")


    # Optimal Approach
    temp = arr.copy()

    # Optimal Approach

    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    temp = arr.copy()

    reverse(temp, 0, n - 1)      # Reverse complete array
    reverse(temp, 0, k - 1)      # Reverse first k elements
    reverse(temp, k, n - 1)      # Reverse remaining elements

    print("\nOptimal Approach")
    print("Array after right rotation:", temp)
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")