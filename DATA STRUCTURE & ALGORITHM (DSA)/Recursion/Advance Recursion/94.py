# Program: Generate All Subsequences With Sum = K

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))


# Brute Force Approach (Generate All Subsequences + Check Sum)

n = len(arr)

print("\nBrute Force Approach")

found = False

for mask in range(1 << n):
    subsequence = []
    total = 0

    for i in range(n):
        if mask & (1 << i):
            subsequence.append(arr[i])
            total += arr[i]

    if total == k:
        print(subsequence)
        found = True

if not found:
    print("No subsequence found")

print("Time Complexity: O(N * 2^N)")
print("Space Complexity: O(N)")


# Better Approach
print("\nBetter Approach")
result_found = False
def generate_subsequence(index, current, current_sum):
    global result_found

    if index == len(arr):
        if current_sum == k:
            print(current)
            result_found = True
        return

    # Take current element
    current.append(arr[index])
    generate_subsequence(index + 1,current,current_sum + arr[index])

    # Not Take current element
    current.pop()
    generate_subsequence(index + 1,current,current_sum)

generate_subsequence(0, [], 0)

if not result_found:
    print("No subsequence found")

print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")


# Optimal Approach (Recursion / Backtracking)
#ye code only tabhi work karega jab array me all elements positive ho
print("\nOptimal Approach")
result_found=[]
def solve(index,total,subset):
    if total==k:
        result_found.append(subset.copy())
        return
    elif total>k:
        return
    if index>=len(arr):
        return
    subset.append(arr[index])
    solve(index+1,total+arr[index],subset)
    
    subset.pop()
    solve(index+1,total,subset)
solve(0,0,[])
print(result_found)
print("Time Complexity: O(2^N)")
print("Space Complexity: O(N)")