# hybrid inheritance
class A:
    def __init__(self,number):
        self.__number = number
    
    def display(self):
        print(f"The number is: {self.__number}")
class B:
    def __init__(self,name):
        self.__name = name

    def show(self):
        print(f"The name is: {self.__name}")
class C(A,B):
    def __init__(self,name,number):
        A.__init__(self,number)
        B.__init__(self,name)
class D(C):
    def __init__(self,name,number):
        super().__init__(name,number)
# creating an object of class D
d = D("Hello", 42)
d.display()  # calling the display method from class A
d.show()     # calling the show method from class B