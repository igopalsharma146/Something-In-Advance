# list comprehension
#comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
print("List comprehension")
l=[1,2,3,4,5]
x=[i**2 for i in l]
print(x)

# list comprehension with if condition
print("\nList comprehension with if condition")
l=[1,2,3,4,5]
x=[i**2 for i in l if i % 2 == 0]
print(x)

# list comprehension with if-else condition
print("\nList comprehension with if-else condition")
l=[1,2,3,4,5]
x=[i**2 if i % 2 == 0 else i**3 for i in l]
print(x)

# list comprehension with nested loops
print("\nList comprehension with nested loops")
l=[1,2,3,4,5]
x=[i*j for i in l for j in l]
print(x)