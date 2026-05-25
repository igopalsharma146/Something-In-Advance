# reference variable
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
person1 = Person("Alice", 30)
# person1 is a reference variable that points to the object created by Person("Alice",30).
person1.display_info()  # Output: Name: Alice, Age: 30