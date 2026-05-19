# oops concept
class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display_info(self):
        print(f"Car Name: {self.name}, Model: {self.model}")
car1 = car("Toyota", "Camry")
car1.display_info()
