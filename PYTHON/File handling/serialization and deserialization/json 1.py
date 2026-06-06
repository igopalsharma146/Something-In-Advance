import json

# Serialization
student = {
    "name": "Gopal",
    "age": 21,
    "course": "AIML"
}

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data1.json", "w") as f:
    json.dump(student, f, indent=4)

print("Object serialized and stored in file")

# Deserialization
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data1.json", "r") as f:
    data = json.load(f)

print(type(data))
print(data)