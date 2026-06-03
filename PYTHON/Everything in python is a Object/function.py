def sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
x=sum
y=[1,2,3,4,5]
l=[1,2,3,4,5,x(y)]
print(l)  # This will print [1, 2, 3, 4, 5, 15], showing that the function sum is treated as an object and can be stored in a list along with its result.

# python me functions bhi objects hote hain, iska matlab hai ki hum functions ko variables me assign kar sakte hain, unhe arguments ke roop me pass kar sakte hain, aur unhe data structures me store kar sakte hain. Iska matlab hai ki functions ke saath bhi hum objects ke jaise kaam kar sakte hain, jise hum higher-order functions kehte hain. Higher-order functions wo functions hote hain jo dusre functions ko arguments ke roop me lete hain ya unhe return karte hain.

def greet(name):
    def inner_greet():
        return f"Hello, {name}!"
    return inner_greet()
greeting = greet("Alice")
print(greeting)  # This will print "Hello, Alice!", showing that the inner function is returned and can be called to get the greeting message.

def outer_function():
    print("This is the outer function.")
    return "Gopal"
    
print(greet(outer_function()))  # This will print "Hello, Gopal!", showing that the outer_function is treated as an object and passed to the greet function.