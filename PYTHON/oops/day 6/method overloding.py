# method overloading
class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c
# creating an object of Calculator
calc = Calculator()

# calling the add method with 2 arguments
result1 = calc.add(2, 3)  # This will raise an error because the add method with 2 parameters is overwritten by the add method with 3 parameters
print(f"Result of adding 2 and 3: {result1}")

# calling the add method with 3 arguments
result2 = calc.add(2, 3, 4)
print(f"Result of adding 2, 3 and 4: {result2}")

# actually, in Python, method overloading is not supported in the traditional sense. The second definition of the add method will overwrite the first one. 
