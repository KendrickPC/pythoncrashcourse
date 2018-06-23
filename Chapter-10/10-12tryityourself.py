# 10-12. Favorite Number Remembered: Combine the two programs from Exercise
# 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the users favorite number and
# store it in a file. Run the program twice to see that it works.

import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! It is " + str(number) + ".")
