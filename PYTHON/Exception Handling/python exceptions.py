#these are some famous exception

# IndexError
# IndexError is thrown when trying to access an item at an invalid index.
l = [1, 2, 3]
print(l[100])

# KeyError
# KeyError is thrown when trying to access a key that does not exist in a dictionary.
d = {"name": "Gopal"}
print(d["age"])

# ValueError
# ValueError is thrown when a function receives an argument of correct type but invalid value.
num = int("hello")

# TypeError
# TypeError is thrown when an operation is performed on incompatible data types.
result = "10" + 10

# ZeroDivisionError
# ZeroDivisionError is thrown when dividing a number by zero.
print(10 / 0)

# NameError
# NameError is thrown when trying to use a variable that is not defined.
print(age)

# FileNotFoundError
# FileNotFoundError is thrown when trying to open a file that does not exist.
f = open("abc.txt", "r")

# ModuleNotFoundError
# ModuleNotFoundError is thrown when importing a module that does not exist.
import mymodule

# AttributeError
# AttributeError is thrown when an object does not have the requested attribute.
s = "hello"
s.append("!")


#some other exceptions
# ImportError
# ImportError is thrown when a specific object cannot be imported from a module.
from math import square

# SyntaxError
# SyntaxError is thrown when Python finds invalid syntax.
if True
    print("Hello")
    
# IndentationError
# IndentationError is thrown when indentation is incorrect.
if True:
print("Hello")

# OverflowError
# OverflowError is thrown when the result of an arithmetic operation is too large.
import math
print(math.exp(1000))

# RecursionError
# RecursionError is thrown when the maximum recursion depth is exceeded.
def func():
    func()

func()

# MemoryError
# MemoryError is thrown when an operation runs out of memory.
l = [1] * (10**20)
