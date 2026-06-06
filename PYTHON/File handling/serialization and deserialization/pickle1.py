#pickle:pickle lets the user to store data in binary format. Json lets the user store data in a human readable text format.
# agar hame data dusri machine me bhejana hai to hum pickle ka use karenge. as a ML Engineer hum Pickle ka use jyada karte h.

# pickling: It is a process where By a object hirarchy is converted in byte stream.
# unpickling: It is the inverse operation where by ab byte stream (from a binary file or bytes like object) is converted back into an object hierarchy.


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