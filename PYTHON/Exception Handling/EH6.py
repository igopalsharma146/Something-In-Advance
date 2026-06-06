# Catching Multiple Exceptions

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")