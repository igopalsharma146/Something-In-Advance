#indirect recursion
def A(n):
    if n==0:
        return 0
    return A(n-1) + B(n-1)

def B(n):
    if n==0:
        return 1
    return B(n-1)+A(n)

x=B(B(2))
print(x)