#seek() = eski help se hum cursor ki position ko change kar sakte h
#tell() = ye hame cursor ki current position batata h 
big_l=["Hello world! " for i in range(1000)]
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample8.txt",'w') as f:
    f.writelines(big_l)

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample8.txt",'r') as f:
    chunk_size=100
    data=f.read(chunk_size)
    print(data,end='')
    print("\ncursor ki current position :",end='')
    print(f.tell()) # cursor ki current position 100
    print(f.seek(10)) # changing the cursor position
    print("\ncursor ki current position :",end='')
    print(f.tell())
    
    
#esme cursor ki position alag aayegi
# kyuki Windows text file me \n ko aksar \r\n (2 characters) ke roop me store karta hai.
# Hello world!  -> 12 characters
# \r\n          -> 2 characters
# ----------------------------
# Total         -> 14 characters
big_l=["Hello world!\n" for i in range(1000)]
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample8.txt",'w') as f:
    f.writelines(big_l)

with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample8.txt",'r') as f:
    chunk_size=100
    data=f.read(chunk_size)
    print(data,end='')
    print("\ncursor ki current position :",end='')
    print(f.tell()) # cursor ki current position 107
    print(f.seek(10)) # changing the cursor position
    print("\ncursor ki current position :",end='')
    print(f.tell())