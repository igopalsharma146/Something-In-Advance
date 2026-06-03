# reduce function
from functools import reduce
def sum(x, y):
    print(f"Adding {x} and {y}...")
    return x + y

l=[1, 2, 3, 4, 5]
x=reduce(sum, l)
print(x)