# docstring in python
def sum(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b

print(sum.__doc__)


print("\n")
# docstring for a class
class Person:
    """This class represents a person with a name and age."""
    
    def __init__(self, name, age):
        """Initialize the person's name and age."""
        self.name = name
        self.age = age

print(Person.__doc__)
print(Person.__init__.__doc__)