# Complete Example
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter only numbers")

except ZeroDivisionError:
    print("Division by zero is not allowed")

except Exception as e:
    print("Some error occurred:", e)

else:
    print("Result:", result)

finally:
    print("Execution finished")