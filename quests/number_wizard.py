import random

secret = random.randint(1, 100)
guess = 0

print("I'm thinking of a number between 1 and 100.")

while guess != secret:
    guess = int(input("Take a guess: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! The number was {secret}.")
