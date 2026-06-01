# generator expression : A generator expression is a concise way to create a generator without the need for a separate function definition. It uses a syntax similar to list comprehensions but with parentheses instead of square brackets. Generator expressions are memory-efficient and can be used in situations where you want to generate values on-the-fly without storing them all in memory at once. An example of a generator expression is shown below:
squares = (x**2 for x in range(10))
for square in squares:
    print(square)