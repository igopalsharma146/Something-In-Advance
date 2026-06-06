import json

def show_object(person):
    if isinstance(person, Person):
        return {
            "fname": person.fname,
            "lname": person.lname,
            "age": person.age,
            "gender": person.gender
        }

# def show_object(person):
#     if isinstance(person, Person):
#         return f"{person.fname} {person.lname} Age -> {person.age} Gender {person.gender}"

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

# Serialization
person = Person("Gopal", "Sharma", 21, "MALE")

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data6.json", "w") as f:
    json.dump(person, f, default=show_object, indent=4)

print("Object serialized and stored in file")

# Deserialization
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data6.json", "r") as f:
    data = json.load(f)

student_obj = Person(**data) # yaha hamare pass jo bhi data aaya , usko constructor ke pass bhej diya hamne

print(type(student_obj))
print(student_obj.fname)
print(student_obj.age)
print(student_obj.gender)