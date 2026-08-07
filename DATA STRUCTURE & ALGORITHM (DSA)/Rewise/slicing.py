# negative slicing in string
text = "Hello, World!"
print(text[-6:-1])  # Output: "World"

k=4
print(text[-k:-1])  # Output: "World"

#reverse slicing in string
print(text[-1:-6:-1])  # Output: "!dlroW"

i=10
while i>0:
    n=int(input("n: "))
    print(~n)
    i-=1