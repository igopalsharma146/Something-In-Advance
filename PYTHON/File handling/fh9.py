# reading and writing binary file
with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\mitrc.jpg",'rb') as f:
    print(f.read())
    f.seek(0)
    with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\mitrc_copy.jpg",'wb') as wb:
        wb.write(f.read())