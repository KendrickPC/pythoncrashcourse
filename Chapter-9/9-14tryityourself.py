# 9-14. Dice: The module random contains functions that generate random
# numbers in a variety of ways. The function randint() returns an
# integer in the range you provide. The following code returns a number
# between 1 and 6:

#   from random import randint
#   x = randint(1, 6)

# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random
# number between 1 and the number of sides the die has. Make a 6-sided
# die and roll it 10 times. Make a 10-sided die and a 20-sided die.
# Roll each die 10 times.

# pep8 compliant

from random import randint


class Die():
    # Representing a die that can be rolled. Sides = 6 by default.
    def __init__(self, sides=6):
        # Initializing the die
        self.sides = sides

    def roll_die(self):
        # Return a number between 1 and sides of Die
        return randint(1, self.sides)

six_sided_dice = Die(sides=6)
results = []
for roll_number in range(10):
    result = six_sided_dice.roll_die()
    results.append(result)
print("10 rolls on a 6-sided die:")
print(results)

ten_sided_dice = Die(sides=10)
results = []
for roll_number in range(10):
    result = ten_sided_dice.roll_die()
    results.append(result)
print("10 rolls on a 10-sided die:")
print(results)

twenty_sided_dice = Die(sides=20)
results = []
for roll_number in range(10):
    result = twenty_sided_dice.roll_die()
    results.append(result)
print("10 rolls on a 20-sided die:")
print(results)
