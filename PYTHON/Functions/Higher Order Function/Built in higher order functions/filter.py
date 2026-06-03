#filter function ek built-in higher-order function hai jo ek iterable ke har element par ek specified function apply karta hai aur ek filter object return karta hai, jise hum list ya kisi aur iterable me convert kar sakte hain.
# filter function ka syntax hai: filter(function, iterable)

# Example of using filter function to get even numbers from a list
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # This will print [2, 4, 6, 8, 10]

# Example of using filter function with a lambda function to get numbers greater than 5 from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = filter(lambda x: x > 5, numbers)
print(list(greater_than_five))  # This will print [6, 7, 8, 9, 10]

#difference between map and filter function
# map function har element par function apply karta hai aur uska result return karta hai, chahe wo result true ho ya false. Filter function sirf un elements ko return karta hai jinke liye function true return karta hai, aur un elements ko ignore karta hai jinke liye function false return karta hai. Iska matlab hai ki map function har element ke liye ek naya value create karta hai, jabki filter function sirf un elements ko select karta hai jo ek condition ko satisfy karte hain.

#example to show the difference between map and filter function
numbers = [1, 2, 3, 4, 5]
# Using map function
mapped_numbers = list(map(lambda x: x * 2, numbers))
print("Mapped numbers:", mapped_numbers)  # This will print [2, 4, 6, 8, 10]

# Using filter function
filtered_numbers = list(filter(lambda x: x > 3, numbers))
print("Filtered numbers:", filtered_numbers)  # This will print [4, 5]

# Using filter function
filtered_numbers = list(filter(lambda x: x + 3, numbers))
print("Filtered numbers:", filtered_numbers) 
# This will print [1, 2, 3, 4, 5] because the lambda function returns a non-zero value for all elements in the list, which is considered true in Python. Therefore, all elements are included in the filtered result.