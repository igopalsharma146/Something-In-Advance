#static method
#static method ko class variable bhi kehte hain, kyunki ye class level method hota hai, aur isme instance variable ka use nahi kar sakte hain. Static method me hum class variable ka use kar sakte hain, isliye hum Employee.counter ka use kar rahe hain. Static method ko hum class name ke through call karte hain, aur isme self ka use nahi karte hain.
class Employee:
    counter =0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    @staticmethod
    def display_count():
        #jab ham static method banate hain to usme self ka use nahi karte hain kyunki static method class level method hota hai, aur usme instance variable ka use nahi kar sakte hain. Static method me hum class variable ka use kar sakte hain, isliye hum Employee.counter ka use kar rahe hain.
        print(f"Total Employees: {Employee.counter}")
    
    @staticmethod
    def get_counter():
        return Employee.counter
    
    @staticmethod
    def set_counter(value):
        if (type(value) == int) and (value >= 0):
            Employee.counter = value
    
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)
Employee.display_count()  # Output: Total Employees: 3
print(Employee.get_counter())  # Output: 3
Employee.set_counter(10)
print(Employee.get_counter())  # Output: 10