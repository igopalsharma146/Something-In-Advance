# Program: Count Frequency of Elements of m Array from n Array

n = [1,2,3,4,2,5,6,7,4,8,9,10,7,5]
m = [11,2,4,77,56,3]


# Brute Force Approach
print("\nBrute Force Approach")

for num in m:
    count = 0

    for element in n:
        if num == element:
            count += 1

    print(f"{num} -> {count}")

print("Time Complexity: O(n*m)")
print("Space Complexity: O(1)")

# Better Approach
print("\nBetter Approach using Dictionary :")

freq = {}

for num in n:
    freq[num] = freq.get(num, 0) + 1

for num in m:
    print(f"{num} -> {freq.get(num, 0)}")

print("Time Complexity: O(n + m)")
print("Space Complexity: O(n)")

# Another Better solution
print("\nBetter Approach using List :")

hash_list=[0]*11
for num in n:
    hash_list[num] += 1
    
for num in m:
    if num<0 or num>10:
        print(f"{num} -> {0}")
    else:
        print(f"{num} -> {hash_list[num]}")
print("Time Complexity: O(n + m)")
print("Space Complexity: O(n)")

# Optimal Approach

print("\nOptimal Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n + m)")
print("Space Complexity: O(n)")