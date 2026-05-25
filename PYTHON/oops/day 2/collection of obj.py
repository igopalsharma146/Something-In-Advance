#collection of objects
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
p1=Student("Alice", 20)
p2=Student("Bob", 22)
p3=Student("Charlie", 21)
students=[p1,p2,p3]  # Collection of Student objects
for student in students:
    student.display_info()  # Call the display_info method of each Student object