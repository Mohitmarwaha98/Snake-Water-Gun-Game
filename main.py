import random

# Randomly select a choice for the computer
computer = random.choice(["snake","water","gun"])

# Mapping user input to game choices
choices = {"s":"snake", "w":"water", "g":"gun"}

# User input with validation
youChoice = input("Enter your choice 's' for Snake, 'w' for Water, 'g' for Gun: ").lower()

if youChoice not in choices:
    print("Invalid Choice")
else:
    you = choices[youChoice]
    print("You chose",you,"\nComputer Chose",computer)

    #Logic
    if computer == you:
        print("Its a draw")
    else:
        if you == "snake" and computer == "water" or you == "water" and computer == "gun" or you == "gun" and computer == "snake":
            print("You Win")
        else:
            print("You Lose")