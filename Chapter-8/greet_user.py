# Passing a List

def greet_user(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['kenderson', 'ken', 'kenneth']
greet_user(usernames)