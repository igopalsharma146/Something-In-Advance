# super keyword in python
#super keyword is used to call the parent class method in the child class
class A:
    def __init__(self,number):
        self.__number = number
    
    def display(self):
        print(f"The number is: {self.__number}")

class B(A):
    def __init__(self,name,number):
        super().__init__(number)  # calling the parent class constructor
        self.__name = name
    def show(self):
        print(f"The name is: {self.__name}")
# creating an object of class B
b = B("Hello", 42)
b.display()  # calling the display method from class A
b.show()     # calling the show method from class B