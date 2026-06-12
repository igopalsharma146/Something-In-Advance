# Bubble sort [Adjacement swap]
# num=[3,5,4,2,6,7,5,9,4]
num=[9,8,7,6,5,4,3,2,1]
n=len(num)
s=0
iteration=0
for i in range(n-2,-1,-1):
    for j in range(0,n-1):
        # print(num)
        iteration+=1
        # print(iteration)
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            s+=1
    # print()
print(num)
print("Total swap :",s)
print("Total iteration:",iteration)



# another method
print()
# num=[3,5,4,2,6,7,5,9,4]
num=[9,8,7,6,5,4,3,2,1]
n=len(num)
s=0
iteration=0
for i in range(1,n):
    for j in range(0,n-1):
        # print(num)
        iteration+=1
        # print(iteration)
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            s+=1
    # print()
print(num)
print("Total swap :",s)
print("Total iteration:",iteration)


# Reducing iteration
print()
num=[9,8,7,6,5,4,3,2,1]
n=len(num)
s=0
iteration=0
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        # print(num)
        iteration+=1
        # print(iteration)
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            s+=1
    # print()
print(num)
print("Total swap :",s)
print("Total iteration:",iteration)


# Best Case
print()
num=[1,2,3,4,5,6,7,8,9]
n=len(num)
s=0
iteration=0
for i in range(n-2,-1,-1):
    is_swap=False
    for j in range(0,i+1):
        # print(num)
        iteration+=1
        # print(iteration)
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            s+=1
            is_swap=True
    if is_swap==False:
        break
    # print()
print(num)
print("Total swap :",s)
print("Total iteration:",iteration)