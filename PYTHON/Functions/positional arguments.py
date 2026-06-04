# Positional arguments are the most common type of arguments in Python. They are passed to a function in the order they are defined. When you call a function, you provide the values for the positional arguments in the same order as they are defined in the function. The number of positional arguments you provide must match the number of parameters defined in the function, otherwise you will get a TypeError.
def add(a, b):
    return a + b
print(add(2, 3))  # Output: 5

def greet(name, message):
    return f"{message}, {name}!"
print(greet("Alice", "Hello"))  # Output: Hello, Alice!

#passing any no. of positional arguments using *args
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5, 6, 7))  # Output: 22