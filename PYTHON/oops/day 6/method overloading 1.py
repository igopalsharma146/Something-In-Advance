# method overloading
class Calculator:
    def area(self, a, b=0):
        if b == 0:
            return a * a  # area of square
        else:
            return a * b  # area of rectangle

# creating an object of Calculator
calc = Calculator()

# calling the area method with 1 argument (square)
result1 = calc.area(5)
print(f"Area of square with side 5: {result1}")

# calling the area method with 2 arguments (rectangle)
result2 = calc.area(5, 3)
print(f"Area of rectangle with length 5 and width 3: {result2}")

#python does not support method overloading in the traditional sense, but we can achieve similar functionality using default parameters or variable-length arguments. In this example, we used a default parameter to allow the area method to calculate the area of both squares and rectangles.