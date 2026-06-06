# Pickle में custom object के लिए __dict__, default, **data जैसी चीज़ों की ज़रूरत नहीं पड़ती। Pickle पूरा object direct save और restore कर देता है।
import pickle

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

# Serialization
person = Person("Gopal", "Sharma", 21, "MALE")

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data7.dat", "wb") as f:
    pickle.dump(person, f)

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data7.pkl", "wb") as f:
    pickle.dump(person, f)

print("Object serialized and stored in file")

# Deserialization
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data7.dat", "rb") as f:
    person_obj = pickle.load(f)

print(type(person_obj))
print(person_obj.fname)
print(person_obj.lname)
print(person_obj.age)
print(person_obj.gender)