# dictionary comprehension is a concise way to create dictionaries in Python. It allows you to generate a new dictionary by applying an expression to each item in an iterable, while optionally filtering items using a condition.
print("Dictionary comprehension")
l=[1,2,3,4,5]
x={i: i**2 for i in l}
print(x)

# dictionary comprehension with if condition
print("\nDictionary comprehension with if condition")
l=[1,2,3,4,5]
x={i: i**2 for i in l if i % 2 == 0}
print(x)

# dictionary comprehension with if-else condition
print("\nDictionary comprehension with if-else condition")
l=[1,2,3,4,5]
x={i: i**2 if i % 2 == 0 else i**3 for i in l}
print(x)

# dictionary comprehension with nested loops
print("\nDictionary comprehension with nested loops")
l=[1,2,3,4,5]
x={i: j for i in l for j in l}
print(x)

print("\nDictionary comprehension internal working")
y=[1,2,3,4,5]
z=dict()
for i in y:
    for j in y:
        # print(i,j)
        z[i]=j
        # print(z)
print(z)

print("\nDictionary comprehension internal working with update method")
y=[1,2,3,4,5]
z=dict()
for i in y:
    for j in y:
        z.update({i:j})
print(z)
#yaha per output {1:1,1:2,1:3,1:4,1:5,2:1,2:2,2:3,2:4,2:5,3:1,3:2,3:3,3:4,3:5,4:1,4:2,4:3,4:4,4:5,5:1,5:2,5:3,5:4,5:5} aayega but dictionary me duplicate keys nahi hoti hai to last key value pair hi store hoga isliye output {1: 5, 2: 5, 3: 5, 4: 5, 5: 5} aayega.