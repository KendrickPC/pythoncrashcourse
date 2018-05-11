# Passing an Arbitrary Number of Arguments

# def make_pizza(*toppings):
# 	"""Print a list of toppings that have been requested."""
# 	print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the parameter name *toppings tells Python 
# to make an empty tuple called toppings and pack whatever 
# values it receives into this tuple. 

# def make_pizza(*toppings):
# 	"""Summarize the pizza we are about to make."""
# 	print("\nMaking a pizza with the following toppings:")
# 	for topping in toppings:
# 		print("- " + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# This syntax works no matter how many 
# arguments the function receives.

# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

# make_pizza(12, 'pepperoni')
# make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')