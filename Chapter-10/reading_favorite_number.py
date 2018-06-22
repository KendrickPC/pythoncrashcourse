import json

with open('favorite_number.json') as favorite:
	number = json.load(favorite)

print("I know your favorite number! It is " + str(number) + ".")
