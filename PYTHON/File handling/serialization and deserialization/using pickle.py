# serialization
import pickle

student = {
    "name": "Gopal",
    "age": 21,
    "course": "AIML"
}

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data.pkl", "wb") as f:
    pickle.dump(student,f)

print("Object serialized and stored in file")


#Deserialization
import pickle

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\serialization and deserialization\data.pkl", "rb") as f:
    data = pickle.load(f)
    print(type(data))

print(data)