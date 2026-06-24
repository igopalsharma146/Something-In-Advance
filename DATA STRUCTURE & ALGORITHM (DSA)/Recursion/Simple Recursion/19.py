#fibonnaci nth term using recursion
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-2)+fib(n-1)
n=int(input("Enter a number :"))
print(fib(n))