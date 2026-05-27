# MRO (Method Resolution Order) is the order in which Python looks for a method in a hierarchy of classes. It is determined by the C3 linearization algorithm, which ensures that the method resolution order is consistent and predictable.
class A:
    def display(self):
        print("This is class A")
class B(A):
    def display(self):
        print("This is class B")
class C(A):
    def display(self):
        print("This is class C")
class D(B,C):
    pass
class E(C,B):
    pass
# creating an object of class D
d = D() 
d.display()  # calling the display method from class D, which will follow the MRO to find the method
# The MRO for class D is: D -> B -> C -> A

# creating an object of class E
e = E()
e.display()  # calling the display method from class E, which will follow the MRO to find the method
# The MRO for class E is: E -> C -> B -> A