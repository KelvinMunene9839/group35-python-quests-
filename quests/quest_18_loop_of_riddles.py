# Quest 18: The Loop of Riddles
# Concept: while loop with user input - keeps asking until the user is correct

secret_number = 7  # The number the user has to guess

guess = None  # Start with no guess so the while condition triggers immediately

while guess != secret_number:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("Correct! You solved the riddle!")
    else:
        print("Wrong! Try again...")
