#Encapsulation
class Car:
    def __init__(self, name, model,price):
        self.__name = name  # Private attribute
        self.__model = model  # Private attribute
        self.price=price  # Public attribute

    def display_info(self):
        print(f"Car Name: {self.__name}, Model: {self.__model}, Price: {self.price}")

car1 = Car("Toyota", "Camry", 25000)

car1.price=30000  # Accessing public attribute
print(car1.price)  # Output: 30000

car1.__name = "Honda"  # Attempting to access private attribute (will not change the name)  
print(car1.__name)  # Output: Honda (but the original name is still "Toyota")

# jab hum python me private variable banate hai to uska naam change ho jata hai, matlab agar hum __name likhte hai to python usko _Car__name me change kar deta hai, isliye jab hum car1.__name = "Honda" likhte hai to actually hum car1._Car__name = "Honda" likh rahe hote hai, aur isse car1 ke original name attribute me koi change nahi hota hai. Isliye jab hum car1.__name print karte hai to hume "Honda" milta hai, lekin jab hum car1.display_info() call karte hai to hume "Toyota" hi milta hai, kyunki display_info method me hum self.__name ko access kar rahe hote hai, jo ki original name attribute ko refer kar raha hota hai.

car1._Car__name = "Honda"  # Accessing private attribute using name mangling
#yaha name mangling ka matlab hai ki hum private attribute ko access karne ke liye uska naam change kar dete hai, jese ki humne car1._Car__name = "Honda" likha hai, isse hum car1 ke original name attribute ko change kar rahe hote hai, aur ab jab hum car1.display_info() call karte hai to hume "Honda" milta hai, kyunki display_info method me hum self.__name ko access kar rahe hote hai, jo ki ab "Honda" ko refer kar raha hota hai.

car1.display_info()