# requested_toppings = 'mushrooms'

# if requested_toppings != 'anchovies':
# 	print("Hold the anchovies!")

# Checking whether a value is in the list

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepporoni' in requested_toppings)

# Sometimes it is important to check all of the conditions of 
# interest. In this case, you should use a series of simple 
# if statements with no elif or else blocks. This technique 
# makes sense when more than one condition could be True, 
# and you want to act on every condition that is True.


# This code would not work properly if we used an if-elif-else 
# block, because the code would stop running after only one test passes.

# In summary, if you want only one block of code to run, use an 
# if-elif- else chain. If more than one block of code needs to run, 
# use a series of independent if statements.

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
# 	print("Adding mushrooms.")
# if 'pepporoni' in requested_toppings:
# 	print("Adding pepporoni.")
# if 'extra cheese' in requested_toppings:
# 	print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# Checking for Special Items
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
# 	if requested_topping == 'green peppers':
# 		print("Sorry. We are out of green peppers.")
# 	else:
# 		print("Adding " + requested_topping + ".")

# print("\nFinished making your pizza!")


# Checking That a List Is Not Empty
# requested_toppings = []

# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		print("Adding " + requested_topping + ".")
# 	print("\nFinished making your pizza.")
# else:
# 	print("Are you sure you want a plain pizza?")


# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
					  'pepporoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("\nAdding " + requested_topping + ".")
	else:
		print("\nSorry, we don't have " + requested_topping + " as a pizza topping.")

print("\nFinished making your pizza!")
