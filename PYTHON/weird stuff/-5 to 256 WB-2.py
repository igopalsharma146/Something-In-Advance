# -5 to 256
a=4
b=4
print(a is b)  # Output: True
print(id(a), id(b))  # Output: Same memory address

print("\nNow let's check the behavior for 257:")
a=257
b=257
print(a is b)  # Output: False
#yah false aana chahiye tha but mere system mein true aa raha hai, iska matlab hai ki mere system mein 257 bhi cache ho raha hai, lekin generally Python ke implementation mein -5 se 256 tak ke integers hi cache hote hain. Iska reason ye hai ki ye small integers bahut commonly use hote hain, isliye Python unhe optimize karne ke liye cache karta hai.
print(id(a), id(b))  # Output: Different memory addresses

# Explanation: In Python, small integers (from -5 to 256) are cached and reused, so variables that reference the same small integer will point to the same memory address. However, integers outside this range are not cached, so each variable referencing a larger integer will point to a different memory address.

print("\nNow let's check the behavior for -5:")
a=-5
b=-5
print(a is b)  # Output: True
print(id(a), id(b))  # Output: Same memory address

print("\nNow let's check the behavior for -6:")
a=-6
b=-6
print(a is b)  # Output: False
# ye bhi true aa raha hai, iska matlab hai ki mere system mein -6 bhi cache ho raha hai
print(id(a), id(b))  # Output: Different memory addresses

print("\nNow let's check the behavior for -20:")
a=-5138900
b=-5138900
print(a is b)  # Output: False
print(id(a), id(b))  # Output: Different memory addresses

print("\nNow let's check the behavior for 1000:")
a=178960
b=178960
print(a is b)  # Output: False
print(id(a), id(b))  # Output: Different memory addresses

a = 1000
b = 1000

print(a == b)   # True
print(a is b)   # Implementation dependent

a=int("1000")
b=int("1000")
print(a == b)   # True
print(a is b)   # Implementation dependent