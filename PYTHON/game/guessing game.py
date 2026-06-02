# guessing game in python
import random

number = random.randint(1, 100)
guess = None
steps = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    steps += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {steps} steps.")