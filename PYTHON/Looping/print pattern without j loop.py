n = 5
for i in range(1, n + 1):
    print("*" * i)

print("\n")
n = 5
for i in range(n, 0, -1):
    print("*" * i)

print("\n")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
    
print("\n")
n = 5
for i in range(1, n + 1):
    print(" " * (i-1) + "*" * (n-i+1))