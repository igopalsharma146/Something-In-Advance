# method overriding
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
# creating objects of Dog and Cat
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!