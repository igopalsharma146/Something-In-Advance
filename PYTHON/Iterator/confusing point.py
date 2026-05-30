l=[1,2,3,4,5]
iter_object1=iter(l)
print(id(iter_object1)," Address of iter_object 1")

iter_object2=iter(iter_object1)
print(id(iter_object2)," Address of iter_object 2")

#eska matlab ye hai ki iter_object1 aur iter_object2 dono same object ko point kar rahe hain, kyunki iter() function agar kisi iterator object ko argument ke roop mein diya jata hai, to wo usi object ko return karta hai. Isliye iter_object1 aur iter_object2 dono ka address same hai.