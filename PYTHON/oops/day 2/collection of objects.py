# Collection of objects
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class School:
    def __init__(self):
        self.students = []  # This will hold a collection of Student objects

    def add_student(self, student):
        self.students.append(student)  # Add a Student object to the collection

    def display_students(self):
        for student in self.students:
            student.display_info()  # Call the display_info method of each Student object
# Create a School object
my_school = School()
# Create some Student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 21)

# Add students to the school
my_school.add_student(student1)
my_school.add_student(student2)
my_school.add_student(student3)

# Display all students in the school
my_school.display_students()