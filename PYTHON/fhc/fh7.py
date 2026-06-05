big_l=["Hello world!\n" for i in range(1000)]
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample7.txt",'w') as f:
    f.writelines(big_l)
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample7.txt",'r') as f:
    chunk_size=10
    data=f.read(chunk_size)
    while len(data)>0:
        print(data,end='')
        data=f.read(chunk_size)
    f.close()