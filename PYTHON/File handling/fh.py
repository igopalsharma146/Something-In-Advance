# file handling
# case 1. : if the file is not present
f=open("C:\Users\Gopal Sharma\Desktop\Restart\PYTHON\File handling\sample.txt",'w')
f.write("Hello World!")
f.close()

# hame file ko close karna jaruri h , kyuki agar file open rahegi to ram me jagah ghere rahegi , kyuki file ram me hi load hoti hai. maan lo yah to ek chhoti si file per ho sakta hai ki compani me hum ek bahut badi file per kaam kare , jaise ki 5gb or 6gb etc. or hamare pass ram only 8gb hai to hamare sare task slow ho jayenge, or another reason agar file open rahegi to koi bhi hacker agar system ko hack kar leta hai to vo uss file ko bhi acess kar lega , jisse hamara data loss bhi ho sakta hai
