try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Custom exception using raise
    if num1 < 0 or num2 < 0:
        raise ValueError("Negative numbers are not allowed")

    result = num1 / num2

except ValueError as e:
    print("ValueError:", e)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except Exception as e:
    print("Some error occurred:", e)

else:
    print("Result:", result)

finally:
    print("Execution finished")
    
    
# raise का उपयोग तब करते हैं जब आप अपनी condition के अनुसार खुद exception generate करना चाहते हैं। For example:
# raise ValueError("Age must be 18 or above")
# raise TypeError("Only integers are allowed")
# raise Exception("Something went wrong")

