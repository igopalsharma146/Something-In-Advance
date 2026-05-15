#exception handling in python
try:
    a=10
    b=0
    c=a/b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", e)