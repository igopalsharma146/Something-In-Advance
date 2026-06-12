#factorial using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)
n=int(input("Enter a number :"))
print(fact(n))

# n=int(input("Enter a number :"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)