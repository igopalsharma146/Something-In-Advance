# map function ek built-in higher-order function hai jo ek iterable ke har element par ek specified function apply karta hai aur ek map object return karta hai, jise hum list ya kisi aur iterable me convert kar sakte hain.
# map function ka syntax hai: map(function, iterable, ...)

# Example of using map function to square each element in a list
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # This will print [1, 4, 9, 16, 25]

# Example of using map function with a lambda function to add 10 to each element in a list
numbers = [1, 2, 3, 4, 5]
added_numbers = map(lambda x: x + 10, numbers)
print(list(added_numbers))  # This will print [11, 12, 13, 14, 15]