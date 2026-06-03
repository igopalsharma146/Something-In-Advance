#Higher order function is a function that takes another function as an argument or returns a function as a result. Higher order functions are a powerful tool in programming, allowing us to create more flexible and reusable code.
# Example of a higher order function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)
# Example of a simple function that can be passed as an argument to the higher order function
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Using the higher order function with different operations
result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)

print("Result of addition:", result1)  # This will print 8
print("Result of multiplication:", result2)  # This will print 15