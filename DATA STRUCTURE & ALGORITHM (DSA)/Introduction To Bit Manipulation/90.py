# Program: Count Bits to Flip (A -> B)

A = int(input("Enter A: "))
B = int(input("Enter B: "))


# Brute Force Approach

xor_result = A ^ B

count = 0

while xor_result > 0:

    if xor_result & 1:
        count += 1

    xor_result >>= 1

print("\nBrute Force Approach")
print("Bits to Flip:", count)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Better Approach
xor_result = A ^ B
binary = bin(xor_result)[2:]
count = binary.count('1')

print("\nBetter Approach")
print("Bits to Flip:", count)

print("Time Complexity: O(log n)")
print("Space Complexity: O(log n)")

# Another Better Approach
print("\nAnother Better Approach")
count=0
ans = A ^ B
for i in range(0,32):
    if ans & (1<<i)!=0:
        count +=1
print(count)
print("Time Complexity: O(32)")
print("Space Complexity: O(1)")

# Optimal Approach
xor_result = A ^ B
count = 0
while xor_result:
    xor_result = xor_result & (xor_result - 1)
    count += 1

print("\nOptimal Approach")
print("Bits to Flip:", count)

print("Time Complexity: O(Number of Set Bits)")
print("Space Complexity: O(1)")

