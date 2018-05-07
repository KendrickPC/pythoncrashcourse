# 7-9 No Pastrami:

# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the 
# list at least three times . Add code near the 
# beginning of your program to print a message 
# saying the deli has run out of pastrami, and 
# then use a while loop to remove all occurrences 
# of 'pastrami' from sandwich_orders . Make sure no
# pastrami sandwiches end up in finished_sandwiches .

sandwich_orders = ['tuna', 'pastrami', 'salmon', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("\nThe deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_orders = sandwich_orders.pop()
	print("Currently making: " + current_orders + " sandwiches.")
	finished_sandwiches.append(current_orders)

print("\nThe following sandwiches have been completed:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)
