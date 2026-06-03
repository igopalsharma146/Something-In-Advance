# reduce function ek built-in higher-order function hai jo ek iterable ke har element par ek specified function apply karta hai aur ek single value return karta hai.
# reduce function ka syntax hai: reduce(function, iterable[, initializer])
from functools import reduce
# Example of using reduce function to get the product of all elements in a list
print("Using reduce function to get the product of all elements in a list...")
def multiply(x, y):
    return x * y
numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print("Product:", product)  # This will print "Product: 120"

# Example of using reduce function with a lambda function to get the greatest element in a list
print("\nUsing reduce function with a lambda function to get the greatest element in a list...")
numbers = [1, 2, 3, 4, 5]
greatest = reduce(lambda x, y: x if x > y else y, numbers)
print("Greatest:", greatest)  # This will print "Greatest: 5"

#example of using reduce function with an initializer to get the sum of all elements in a list
print("\nUsing reduce function with an initializer to get the sum of all elements in a list...")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers, 0)
print("Total:", total)  # This will print "Total: 15"  

#difference between reduce and other higher-order functions like map and filter
# map function har element par function apply karta hai aur uska result return karta hai, chahe wo result true ho ya false. Filter function sirf un elements ko return karta hai jinke liye function true return karta hai, aur un elements ko ignore karta hai jinke liye function false return karta hai. Reduce function ek iterable ke har element par function apply karta hai aur ek single value return karta hai, jo ki iterable ke elements ka cumulative result hota hai. Iska matlab hai ki map function har element ke liye ek naya value create karta hai, filter function sirf un elements ko select karta hai jo ek condition ko satisfy karte hain, aur reduce function ek single value return karta hai jo ki iterable ke elements ka cumulative result hota hai.

#example to show the difference between reduce, map and filter function
print("\nExample to show the difference between reduce, map and filter function...")
numbers = [1, 2, 3, 4, 5]
# Using map function to double each element in the list
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)  # This will print "Doubled: [2, 4, 6, 8, 10]"

# Using filter function to get only even numbers from the list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)  # This will print "Evens: [2, 4]"

# Using reduce function to get the sum of all elements in the list
total = reduce(lambda x, y: x + y, numbers)
print("Total:", total)  # This will print "Total: 15"


