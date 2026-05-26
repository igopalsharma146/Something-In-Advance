#polymorphism method overridding
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def login(self):
        print(f"{self.name} has logged in.")
        
class admin(user):
    def login(self):
        print(f"{self.name} is {self.age} years old.")
# creating an object of the admin class
admin_user = admin("Alice", 30)
admin_user.login()  # calling the login method from the admin class, which overrides the login method from the user class