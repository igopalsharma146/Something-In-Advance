#pass by reference
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
def update_person(person):
    print(id(person))  # Print the memory address of the person object
    person.name = "Bob"  # Modifying the name attribute of the person object
    person.age = 25      # Modifying the age attribute of the person object
    print(id(person))  # Print the memory address again to show that it is the same as before, confirming that we are modifying the same object
    
person1 = Person("Alice", 30)
print(id(person1))  # Print the memory address of person1 to show that it is the same as the one in update_person function
print("Before update:")
person1.display_info()

update_person(person1)
#passing person1 to the update_person function allows us to modify the original object that person1 references. This is because in Python, objects are passed by reference, meaning that the function receives a reference to the same object in memory. Therefore, any changes made to the object within the function will affect the original object outside the function.
print("After update:")
person1.display_info()


#class ke object ko pass by reference ke through modify kar sakte hain, kyunki class ke objects mutable hote hain. Jab hum kisi function ko class ke object ko pass karte hain, toh function usi object ka reference receive karta hai. Iska matlab hai ki function ke andar kiye gaye changes original object par reflect honge, kyunki dono function aur original variable same memory location ko point karte hain.