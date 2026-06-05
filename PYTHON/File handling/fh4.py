#writing multiple lines
l=["Hello world!","\nMy name is gopal sharma.","\tI am from alwar."]
f=open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample4.txt",'w')
f.writelines(l)
f.close()