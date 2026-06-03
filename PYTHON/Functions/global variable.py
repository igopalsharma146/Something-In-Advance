# global variable
x = 10  # x is a global variable
def my_function():
    print("Value of x inside the function:", x)
my_function()
print("Value of x outside the function:", x)  # This will print 10, showing that x is a global variable
#hum global variable ko function ke andar bhi access kar sakte hain, but agar hum function ke andar x ko modify karne ki koshish karte hain, toh hume global keyword ka use karna padega.


#hum global variable ko function ke andar access to kar sakte h per usko modify karne ke liye global keyword ka use karna padega. Agar hum global keyword ka use nahi karte hain, toh function ke andar x ek local variable ban jayega aur global variable x ko modify nahi karega.
print("\nTrying to modify global variable y inside the function without using global keyword...")
y=10
def modify_local():
    # y+=20  # This will show an error because we can't modify a global variable without declaring it as global inside the function
    print("Value of y inside the function:", y)  # This will print 30, showing that y is a local variable
modify_local()


print("\nModifying global variable x inside the function...")
def modify_global():
    global x  # Declare x as global to modify it
    x = 20  # This will modify the global variable x
modify_global()
print("Value of x after modification:", x)  # This will print 20, showing

