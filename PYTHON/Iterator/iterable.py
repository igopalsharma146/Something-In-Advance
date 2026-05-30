# iterable : An iterable is an python object, which one can iterate over. it generates an iterator when passed to the iter() function. 


#iteration : in simple words, iteration is the process of traversing through a sequence of data, one item at a time. 
#iterator : An iterator is a object that allow the programmer to traverse through a sequence of data without having to store the entire data in memory. matlab eski help se hum ek ek item ko access kar sakte hai, bina poore data ko memory me store kiye hue.
#iterable : An iterable is an object that can be iterated over, meaning that you can traverse through all the values. matlab iterable object wo hota hai jiske andar hum ek ek item ko access kar sakte hai, bina poore data ko memory me store kiye hue.


# example of iterable
my_list = [1, 2, 3, 4, 5]
print(type(my_list)) # this will show the type of the object, which is list, and list is an iterable object.

print(iter(my_list)) # this will return an iterator object, which we can use to iterate over the list.
print(type(iter(my_list))) # this will show the type of the object, which is list_iterator, and list_iterator is an iterator object.

# my_list is an iterable 
#iter(my_list) is an iterator object, which we can use to iterate over the list.


#point to note : 
# every iterator is an iterable but not every iterable is an iterator.

#Trick : 1. every iterable has an iter() function, 2. every iterator has both iter() and next() function. 

# iterable : iterable ka pata lagane ke 2 tarike h , uske uper loop chala ke dekh lo, agar loop chal jata hai to wo iterable hai, aur dusra tarika ye hai ki uss variable ya object ko dir() function ke andar daal ke dekh lo, agar usme __iter__() function hai to wo iterable hai.

# iterator : variable ya object ko dir() function ke andar daal ke dekh lo, agar usme __iter__() aur __next__() function hai to wo iterator hai.

l=[1,2,3,4,5]
print(dir(l)) # this will show all the attributes and methods of the list object, and we can see that there is __iter__() function but there is no __next__() function, so list is an iterable but not an iterator.
x=iter(l)
print(dir(x)) # this will show all the attributes and methods of the list_iterator object, and we can see that there is both __iter__() and __next__() function, so list_iterator is an iterator.

#iss tarah se hum iterable aur iterator ka pata laga sakte hai, aur unke beech ke difference ko samajh sakte hai. or iterable ko iter() function ke andar daal ke uska iterator bana sakte hai.