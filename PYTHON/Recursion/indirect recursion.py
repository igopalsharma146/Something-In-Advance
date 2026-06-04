def funcA(n):
    if n>0:
        print(n)
        funcB(n//5)

def funcB(n):
    if n>0:
        print(n)
        funcA(n-1)
funcA(20)