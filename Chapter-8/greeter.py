# Defining a Function

def greet_user(username):
	"""docstring comment with triple quotes"""
	print("Hello " + username.title() + "!")

greet_user('antdoggy')
greet_user('brotherkendrick')
greet_user('kendrickpc')

# People sometimes speak of arguments and parameters 
# interchangeably. Don not be surprised if you see the 
# variables in a function definition referred to as 
# arguments or the variables in a function call referred
# to as parameters.