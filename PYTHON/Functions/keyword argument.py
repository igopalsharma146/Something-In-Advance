# keyword arguments are a way to pass arguments to a function by explicitly specifying the parameter names. This allows you to provide arguments in any order, and it can make your code more readable and easier to understand. When you use keyword arguments, you can also provide default values for parameters, which will be used if the caller does not provide a value for that parameter.
def greet(name, message="Hello"):
    return f"{message}, {name}!"
print(greet(name="Alice", message="Hi"))  # Output: Hi, Alice!
print(greet(message="Welcome", name="Bob"))  # Output: Welcome, Bob!

# Keyword arguments with default values
def greet(name, message="Hello"):
    return f"{message}, {name}!"
print(greet(name="Charlie"))  # Output: Hello, Charlie!
print(greet(name="gopal"))  # Output: Hello, gopal!

# Keyword arguments with *args and **kwargs
def greet(name, message="Hello", *args, **kwargs):
    extra_info = ", ".join(args) if args else ""
    extra_kwargs = ", ".join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else ""
    return f"{message}, {name}! {extra_info} {extra_kwargs}"
