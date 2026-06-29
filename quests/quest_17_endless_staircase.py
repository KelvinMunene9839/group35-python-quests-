# Quest 17: The Endless Staircase
# Concept: while loop - keeps running as long as the condition is True

count = 0  # Start the counter at 0

while count < 5:  # Keep looping while count is less than 5
    print(f"Count is: {count}")
    count += 1    # Increase counter by 1 each time to avoid infinite loop

print("The staircase has ended! Final count:", count)
