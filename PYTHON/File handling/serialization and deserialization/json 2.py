import json

# Serialization in list
students = ["Gopal", "Rahul", "Aman", "Priya"]

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data2.json", "w") as f:
    json.dump(students, f, indent=4)

print("List serialized and stored in file")

# Deserialization in list
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data2.json", "r") as f:
    data = json.load(f)

print(type(data))
print(data)