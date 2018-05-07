responses = {}

# Setting flag to indicate that polling is active
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = raw_input("\nWhat is your name? ")
	response = raw_input("Which mountain would you like to climb for your bucketlist? ")
	# Store the response in the dictionary:
	responses[name] = response

	# Find out if anyone else is going take the poll
	repeat = raw_input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb the " + response + ".")