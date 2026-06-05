with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\video.mp4",'rb') as f:
    print(f.read())
    f.seek(0)
    with open(r"C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\video_copy.mp4",'wb') as wb:
        wb.write(f.read())