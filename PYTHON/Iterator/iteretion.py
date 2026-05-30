# iteration : iteration is a general term for taking each item of something, one after another. Any time we use a loop, explicitly or implicitly, to go over a group of items, that is iteration. In python, we can iterate over a list, tuple, string, dictionary, set and even file objects.
# iterator : An iterator is a general term for an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# iterable : An iterable is any Python object capable of returning its members one at a time, allowing it to be iterated over in a for-loop. 

# example of iteration
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)