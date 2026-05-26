# Aggregation relationship in OOPs
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, engine):
        self.engine = engine
# Creating an Engine object
engine = Engine(150)
# Creating a Car object with the Engine object
car = Car(engine)
# Accessing the horsepower of the engine through the car object
print(f"The car has an engine with {car.engine.horsepower} horsepower.")