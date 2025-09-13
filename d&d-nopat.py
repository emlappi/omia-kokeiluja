import random
from operator import truediv

#let´s ask from the user what and how many of the selected die they want to use
dice = int(input("How many sides is on your die?\n"))
times = int(input("How many dices do you want to use?\n"))

# we will use for loop that was suggested by my fiance
for x in range(times):
    amount = random.randint(1, dice)
    print(f"Dice {x+1} gave {amount}")

# let´s ask from the user if they want to throw again
question = input("Do you want to throw again Y/N?\n"")
import random
from operator import truediv

#let´s ask from the user what and how many of the selected die they want to use
dice = int(input("How many sides is on your die?\n"))
times = int(input("How many dices do you want to use?\n"))

# we will use for loop that was suggested by my fiance
for x in range(times):
    amount = random.randint(1, dice)
    print(f"Dice {x+1} gave {amount}")

# let´s ask from the user if they want to throw again
    question = input("Do you want to throw again Y/N?\n")
    question = true:
            if question == "Y" or question == "y":

                dice = int(input("How many sides is on your die?\n"))
                times = int(input("How many dices do you want to use?\n"))

                for x in range(times):
                    amount = random.randint(1, dice)
                    print(f"Dice {x+1} gave {amount}")


        else:
            print("Thank you for throwing dice")
# en oikee tiiä miten saisin tän toimimaan
# tavoite olis että saatais toimimaan toi if looppi
looppi dooppi