# strings
# pahle agar given string ek valid identifier ho tab hi unka address same hota tha, otherwise unka address alag hota tha, lekin ab aisa nahi hai, ab strings bhi cache ho rahe hain, chhote strings to hamesha cache hote hain, lekin bade strings bhi cache ho sakte hain, ye implementation pe depend karta hai.


a = "hello"
b= "hello"
print(a is b)  # Output: True
print(id(a), id(b))  # Output: Same memory address

print("\nNow let's check the behavior for a longer string:")
a = "hello, world!"
b = "hello, world!"
print(a is b)  # Output: True
print(id(a), id(b))  # Output: Same memory address

print("\nNow let's check the behavior for a very long string:")
a="go ti thw hsfj sduygfue asjdgfuys sjdfgweu sjgfy go to the hell and die"
b="go ti thw hsfj sduygfue asjdgfuys sjdfgweu sjgfy go to the hell and die"
print(a is b)  # Output: Implementation dependent
print(id(a), id(b))  # Output: Implementation dependent
