import random
from operator import truediv

#let´s ask from the user what and how many of the selected die they want to use
dice = int(input("How many sides is on your die?:\n"))
times = int(input("How many of dices do you want to use:?\n"))

# we will use for loop that was suggested by my fiance
for x in range(times):
    amount = random.randint(1, dice)
    print(f"Dice {x+1} gave {amount}")
