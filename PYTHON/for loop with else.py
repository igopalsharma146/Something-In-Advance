# for loop with else
for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")
    
print("\n")
# for loop with else and break
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print(i)
else:
    print("Loop completed successfully.")
    
print("\n")
# for loop with else and continue
for i in range(5):
    if i == 3:
        print("Continuing the loop at i =", i)
        continue
    print(i)
else:
    print("Loop completed successfully.")