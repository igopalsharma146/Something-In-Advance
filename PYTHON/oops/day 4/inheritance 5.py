# inheritance problem
class A:
    def __init__(self):
        print("This is class A")
        self.number = 100
        
    def display1(self,number):
        #yaha number ko access karne ke liye self.number ka use karna hoga, kyunki number class A ka attribute hai
        print(f"The number is: {self.number}")
        
class B(A):
    def display2(self,number):
        print(f"This is class B and the number is: {self.number}")

# creating an object of class B
b = B()
b.display1(42)  # calling the display1 method from class A
