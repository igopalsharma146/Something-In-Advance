# Program: Two Sum

arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target sum: "))


# Brute Force Approach
found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("\nBrute Force Approach")
            print(f"Indices: {i}, {j}")
            print(f"Elements: {arr[i]}, {arr[j]}")
            found = True
            break

    if found:
        break

if not found:
    print("\nBrute Force Approach")
    print("No pair found")

print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Better Approach
hash_map = {}
found = False

for i in range(len(arr)):
    complement = target - arr[i]

    if complement in hash_map:
        print("\nBetter Approach")
        print(f"Indices: {hash_map[complement]}, {i}")
        print(f"Elements: {complement}, {arr[i]}")
        found = True
        break

    hash_map[arr[i]] = i

if not found:
    print("\nBetter Approach")
    print("No pair found")

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")