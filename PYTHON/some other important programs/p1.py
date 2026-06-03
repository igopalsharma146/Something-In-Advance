# taking infinite number of arguments from the user
def sum(*args):
    print(type(args)) # <class 'tuple'>
    s=0
    for i in args:
        s+=i
    print(s)
sum(1,2,3,4,5)
sum(1,2,3)

# taking infinite number of string arguments from the user
def print_strings(*args):
    print(type(args)) # <class 'tuple'>
    for s in args:
        print(s)
print_strings("Hello", "World", "Python")

# taking infinite number of keyword arguments from the user
def print_kwargs(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Alice", age=30, city="New York")