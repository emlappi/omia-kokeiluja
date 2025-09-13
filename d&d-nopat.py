import random
from operator import truediv

#let´s ask from the user what and how many of the selected die they want to use
dice = int(input("How many sides is on your die?:\n"))
times = int(input("How many of dices do you want to use:?\n"))

# there are dices with unlimited amount of sides
sides = random.randint(1,dice)

#we will use for loop
