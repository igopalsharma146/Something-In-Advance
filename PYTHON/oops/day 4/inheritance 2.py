#inheritance with private members
class user:
    def __init__(self,name,age):
        self.__name = name  # private member
        self.__age = age    # private member
    
    def login(self):
        print(f"{self.__name} has logged in.")
        print(f"{self.__name} is {self.__age} years old.")
class admin(user):
    def __init__(self,name,age,admin_level):
        super().__init__(name, age)
        self.__admin_level = admin_level  # private member
    
    def access_admin_panel(self):
        print(f"{self._user__name} has accessed the admin panel with level {self.__admin_level}.")
# creating an object of the admin class
admin_user = admin("Alice", 30, "superadmin")
admin_user.login()  # calling the login method from the user class
admin_user.access_admin_panel()  # calling the access_admin_panel method from the admin class