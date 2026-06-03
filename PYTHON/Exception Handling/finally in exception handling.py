# finally in exception Handling
try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("This will always be executed.")
    
print("\n")
# diffrence b/w print and finally
try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", e)
print("This will always be executed.")

print("\n")
def fin():
    try:
        a = 10
        b = 0
        c = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("An error occurred:", e)
print("This will always be executed.")
fin()

#finally block is used to execute the code which is always executed whether an exception occurs or not. It is used to clean up the resources or to close the files or to release the locks. It is also used to execute the code which is required to be executed after the try block.
#finally block function me value return hone ke baad bhi run hota hai. Agar try block me return statement hai to finally block ke baad return statement execute hota hai. Agar try block me exception aata hai to finally block ke baad exception raise hota hai. Agar try block me exception nahi aata hai to finally block ke baad normal execution hota hai.

print("\n")
def fin():
    try:
        a = 10
        b = 0
        c = a / b
        return c
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("This will always be executed....")
fin()

#Agar try block me exception aata hai to finally block ke baad exception raise hota hai. Agar try block me exception nahi aata hai to finally block ke baad normal execution hota hai. Agar try block me return statement hai to finally block ke baad return statement execute hota hai.
print("\n")
def fin():
    try:
        a = 10
        b = 0
        c = a / b
        return c
    finally:
        print("This will always be executed....")
fin()



