# #reading
# f=open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample5.txt",'r')
# x=f.read()
# print(x)
# f.close()

# #reading lines
# f=open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample5.txt",'r')
# x=f.readline()
# print(x,end='')
# x=f.readline()
# print(x,end='')
# f.close()

# #reading entire lines
# f=open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample5.txt",'r')
# data=f.readline()
# while data !='':
#     print(data,end='')
#     data=f.readline()
# f.close()

#reading entire lines
f=open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample5.txt",'r')
while True:
    data=f.readline()
    if data=='':
        break
    else:
        print(data,end='')
f.close()