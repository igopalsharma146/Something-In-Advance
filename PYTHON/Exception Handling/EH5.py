# finally block executes whether an exception occurs or not.

try:
    f = open("sample.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("This block always executes")