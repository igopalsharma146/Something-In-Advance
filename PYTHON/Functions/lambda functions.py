# lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code.
# The syntax for a lambda function is:
# lambda arguments: expression
# lambda input: expression

# Example of a lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # This will print 8

# Example of a lambda function that squares a number
square = lambda x: x ** 2   
print(square(4))  # This will print 16

#Different in between normal function and lambda function
# 1. A normal function is defined using the def keyword, while a lambda function is defined using the lambda keyword.
# 2. A normal function can have multiple expressions and statements, while a lambda function can only have one expression.
# 3. A normal function can be named, while a lambda function is anonymous (it does not have a name).
# 4. A normal function can be reused multiple times in the code, while a lambda function is typically used for short, one-time operations and is not reused elsewhere in the code.
