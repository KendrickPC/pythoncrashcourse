# Defining a Function

# def greet_user(username):
# 	"""docstring comment with triple quotes"""
# 	print("Hello " + username.title() + "!")

# greet_user('antdoggy')
# greet_user('brotherkendrick')
# greet_user('kendrickpc')

# People sometimes speak of arguments and parameters 
# interchangeably. Don not be surprised if you see the 
# variables in a function definition referred to as 
# arguments or the variables in a function call referred
# to as parameters.

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = raw_input("First name: ")
	if f_name == 'q':
		break
	l_name = raw_input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")