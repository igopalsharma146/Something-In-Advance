# zip function is used to combine two or more iterables (like lists, tuples, etc.) into a single iterable of tuples. Each tuple contains the elements from the input iterables that are at the same position.
# The zip function takes iterables as arguments and returns an iterator of tuples. The length of the resulting iterator is equal to the length of the shortest input iterable. If the input iterables are of different lengths, the zip function will stop creating tuples when the shortest iterable is exhausted.
print("Zip function")
l1=[1,2,3]
l2=['a','b','c']
z=zip(l1,l2)
print(z) # <zip object at 0x7f8c8c8c8c0>
print(list(z)) # [(1, 'a'), (2, 'b'), (3, 'c')]

for i in zip(l1,l2):
    print(i) # (1, 'a') (2, 'b') (3, 'c')