#inheritance
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def login(self):
        print(f"{self.name} has logged in.")
class admin(user):
    def __init__(self,name,age,admin_level):
        super().__init__(name, age)
        self.admin_level = admin_level
    
    def access_admin_panel(self):
        print(f"{self.name} has accessed the admin panel with level {self.admin_level}.")
# creating an object of the admin class
admin_user = admin("Alice", 30, "superadmin")
admin_user.login()  # calling the login method from the user class
admin_user.access_admin_panel()  # calling the access_admin_panel method from the admin class