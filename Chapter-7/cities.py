# Using break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: 
	city = raw_input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + " with you!")

# You can use the break statement in any of Pythons loops. 
# For example, you could use break to quit a for loop that is
# working through a list or a dictionary.