import random

# Randomly select a choice for the computer
computer = random.choice([1,0,2])

# Mapping user input to game choices
youDict = {"s":0, "w":1, "g":2}
revDict = {0:"Snake", 1:"Water", 2:"Gun"}

# User input with validation
youChoice = input("Enter your choice 's' for Snake, 'w' for Water, 'g; for Gun: ").lower()
if youChoice not in youDict:
    print("Invalid Choice")
else:
    you = youDict[youChoice]
    print("You chose",revDict[you],"\nComputer Chose",revDict[computer])

    #Logic
    if computer == you:
        print("Its a draw")
    else:
        if computer == 0 and you == 1:
            print("You Lose")
        elif computer == 0 and you == 2:
            print("You Won")
        elif computer == 1 and you == 0:
            print("You Won")
        elif computer == 1 and you == 2:
            print("You Lose")
        elif computer == 2 and you == 0:
            print("You Lose")
        elif computer == 2 and you == 1:
            print("You Win")
        else:
            print("Something went wrong")