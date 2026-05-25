#instance variable in python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        self.display_info()
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)