#static method is a method that belongs to the class rather than the instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator.
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Calling static methods on the class itself
result_add = MathOperations.add(5, 3)
result_subtract = MathOperations.subtract(5, 3)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")