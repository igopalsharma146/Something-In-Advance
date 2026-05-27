# multilevel inheritance
class A:
    def __init__(self,number):
        self.__number = number
    
    def display(self):
        print(f"The number is: {self.__number}")
class B(A):
    def __init__(self,name,number):
        super().__init__(number)
        self.__name = name
    def show(self):
        print(f"The name is: {self.__name}")
class C(B):
    def __init__(self,name,number):
        super().__init__(name,number)
# creating an object of class C
c = C("Hello", 42)
c.display()  # calling the display method from class A
c.show()     # calling the show method from class B