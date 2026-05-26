#static variable with private access
class Employee:
    __counter = 0  # private static variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__counter += 1  # incrementing the private static variable

    @staticmethod
    def display_count():
        print(f"Total Employees: {Employee.__counter}")  # accessing the private static variable
    @staticmethod
    def get_counter():
        return Employee.__counter  # accessing the private static variable
    @staticmethod
    def set_counter(value):
        if (type(value) == int) and (value >= 0):
            Employee.__counter = value  # modifying the private static variable
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)
Employee.display_count()  # Output: Total Employees: 3
print(Employee.get_counter())  # Output: 3
Employee.set_counter(10)
print(Employee.get_counter())  # Output: 10