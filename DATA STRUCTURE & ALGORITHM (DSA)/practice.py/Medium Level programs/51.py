# 3 sum
arr = [1,2,0,-1,2,-2,3,1,-4,0,-1]
n = len(arr)

result = set()

for i in range(n):
    my_set = set()

    for j in range(i+1, n):
        target = -(arr[i] + arr[j])

        if target in my_set:
            result.add(tuple(sorted((arr[i], arr[j], target))))
        else:
            my_set.add(arr[j])

print(result)