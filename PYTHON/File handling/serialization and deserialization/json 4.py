import json

# Serialization in tuple
student = ("Gopal", 21, "AIML")

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data4.json", "w") as f:
    json.dump(student, f, indent=4)

print("Tuple serialized and stored in file")

# Deserialization in tuple
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data4.json", "r") as f:
    data = tuple(json.load(f))

print(type(data))
print(data)

