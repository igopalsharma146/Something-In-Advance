# Optimal Approach of Two Unique Numbers in Array
arr=[2,3,4,5,3,2]
unique = 0

for num in arr:
    unique ^= num
print(unique)
# print(4^5) #    4 -> 0100
            #     5 -> 0101
        # result= 1 -> 0001
        # hamre result ki right most bit 1 hai , to eska matlab hai ki hamre array me 0 or 1 ka bit ka xor huaa h, to hum poore array ko ess bit se And operation karke 2 group bana lenge or unn dono group ka alag alag xor karke hum vo unique number find kar sakte h


# Program: Find Two Unique Numbers in Array
print("\n")
arr = [2, 3, 4, 6, 3, 2]

xor_result = 0

for num in arr:
    xor_result ^= num

print("xor result :",xor_result)
rightmost_set_bit = xor_result & -xor_result # -xor_result ka matlab h 2's complement
print("right most bit :",rightmost_set_bit)

num1 = 0
num2 = 0

for num in arr:
    if num & rightmost_set_bit:
        num1 ^= num
    else:
        num2 ^= num

print("Unique Numbers:", num1, num2)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")