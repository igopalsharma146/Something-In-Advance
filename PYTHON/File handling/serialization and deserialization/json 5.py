import json

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student = Student("Gopal", 21, "AIML")

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data5.json", "w") as f:
    json.dump(student, f, indent=4)
    
# Custom object को json.dump() सीधे serialize नहीं कर सकता।

