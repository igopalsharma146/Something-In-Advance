# Encapsulation with getter and setter methods
class Car:
    def __init__(self, name, model, price):
        self.__name = name  # Private attribute
        self.__model = model  # Private attribute
        self.price = price  # Public attribute

    def display_info(self):
        print(f"Car Name: {self.__name}, Model: {self.__model}, Price: {self.price}")

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        self.__model = model
car=Car("Toyota", "Camry", 25000)
car.display_info()  # Output: Car Name: Toyota, Model: Camry, Price: 25000
car.get_name()  # Output: Toyota
car.set_name("Honda")
car.get_model()  # Output: Camry
car.set_model("Civic")  