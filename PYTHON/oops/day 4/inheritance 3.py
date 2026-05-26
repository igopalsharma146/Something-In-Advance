#inheriting the constructor of the parent class
class A:
    def __init__(self):
        print("This is class A")

class B(A):
    pass
# creating an object of class B
b = B()