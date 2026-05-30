#iterator : An iterator is a object that allow the programmer to traverse through a sequence of data without having to store the entire data in memory. 

# example of iterator

#iteration example
import sys
l= [ x for x in range(1,10000)]
# for i in l:
#     print(i)
print(sys.getsizeof("size of list : " + str(l))) # this will show the size of the list in memory
# yaha per string ke size ko bhi calculate kar rahe hai kyuki list ka size calculate karne ke liye hume string me convert karna padta hai, aur string ka size bhi memory me store hota hai, isliye string ke size ko bhi calculate karna padta hai.
print(sys.getsizeof(l))


#iterator example
x=range(1,10000)
print(sys.getsizeof("size of range : " + str(x))) # this will show the size of the range object in memory
print(sys.getsizeof(x)) 