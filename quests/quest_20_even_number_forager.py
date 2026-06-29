# Quest 20: The Even Number Forager
# Concept: if statement inside a for loop
# A number is even if it has NO remainder when divided by 2 (num % 2 == 0)

print("Even numbers from 1 to 20:")

for num in range(1, 21):
    if num % 2 == 0:
        print(num)
