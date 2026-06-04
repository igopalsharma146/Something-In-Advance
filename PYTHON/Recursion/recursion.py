def fib(num):
    if num==1:
        return 0
    if num==2:
        return 1
    return fib(num-2)+fib(num-1)
x=fib(5)
print(x)
    
# printing Nth term
n = 10
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
    
print("\n")
def fib(num):
    if num==1:
        return 0
    if num==2:
        return 1
    return fib(num-2)+fib(num-1)
for i in range(1,10):
    print(fib(i))