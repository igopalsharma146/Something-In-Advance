#inheritance
class A:
    def __init__(self):
        print("This is class A")

class B(A):
    def __init__(self):
        super().__init__()
        # calling the constructor of class A using super() function
        print("This is class B")
# creating an object of class B
b = B()