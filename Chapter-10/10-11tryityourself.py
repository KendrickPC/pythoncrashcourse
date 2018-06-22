# 10-11. Favorite Number: Write a program that prompts for the users favorite
# number. Use json.dump() to store this number in a file. Write a separate
# program that reads in this value and prints the message, I know your
# favorite number! It is _____ .

import json

prompt = input("What is your favorite number? ")

with open('favorite_number.json', 'w') as favorite:
	json.dump(prompt, favorite)
	print("Thanks! I'll remember that.")
