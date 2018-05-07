# 7-4 Pizza Toppings

prompt = "\nWhat toppings would you like to have on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	pizza_topping = raw_input(prompt)

	if pizza_topping == 'quit':
		break
	else:
		print("Adding " + pizza_topping + " for you on your pizza.")