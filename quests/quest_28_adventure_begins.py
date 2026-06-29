# Quest 28: The Adventure Begins
# Text-based choose-your-own-adventure with functions for each location.

def start():
    print("\nYou stand at the entrance of a dark forest.")
    choice = input("Do you go 'deeper' into the forest or 'turn back'? ")
    if choice == "deeper":
        forest_clearing()
    else:
        ending_safe()

def forest_clearing():
    print("\nYou reach a moonlit clearing. A dragon sleeps on a pile of gold.")
    choice = input("Do you 'sneak' past or try to 'fight' the dragon? ")
    if choice == "sneak":
        ending_treasure()
    else:
        ending_dragon()

def ending_treasure():
    print("\nYou sneak past the dragon and find a hidden door behind the gold pile.")
    print("Inside is a room full of even MORE treasure. You win! (Ending 1: The Clever Hero)")

def ending_dragon():
    print("\nThe dragon wakes up and roars. You run as fast as you can... and escape just in time.")
    print("You leave empty-handed but alive. (Ending 2: The Lucky Escape)")

def ending_safe():
    print("\nYou decide the forest is too dangerous and go home.")
    print("You live a long and peaceful life. (Ending 3: The Wise Choice)")

print("=== The Adventure Begins ===")
start()
