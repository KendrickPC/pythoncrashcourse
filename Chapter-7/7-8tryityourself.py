# 7-8 Deli:

sandwich_orders = ['tuna', 'salmon', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
	current_orders = sandwich_orders.pop()

	print("Currently making: " + current_orders + " sandwiches.")
	finished_sandwiches.append(current_orders)

print("\nThe following sandwiches have been completed:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)