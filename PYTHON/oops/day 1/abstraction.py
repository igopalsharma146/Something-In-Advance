# hiding details

# abstract class banane ke liye 2 cheeje honi jaruri h, ek class abstract class tab banegi tab ye
# 1. ABC class se inherit karegi
# 2. class me kam se kam ek abstract method hona chahiye
# abstract method ke ander kuch bhi likha nahi hota hai bas @abstractmethod likha hota hai
# abstract class me ek database bhi hota hai jisse vpo details fetch karta hai


from abc import ABC,abstractmethod
class BankApp(ABC):
    def database(self):
        print("conected to the database.")
    
    @abstractmethod
    def security(self):
        pass
    
class MobileApp(BankApp):
    def mobile_login(self):
        print("Login sucessfully !.")

    def security(self):              # jab tak ham security method define nhi karenge tab tak ye code run nahi hoga , kyuki security method ek abstract method h
        print("Mobile security")
obj=MobileApp()
obj.database()
