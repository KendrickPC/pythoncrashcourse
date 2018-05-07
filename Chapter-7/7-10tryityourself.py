# 7-10 Dream Vacation:

# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in
# the world, where would you go? Include a block of code that
# prints the results of the poll.

responses = {}

# Setting flag to indicate that polling is active
polling_active = True

while polling_active:
	# Prompt for the person's name and response
	name_poll = raw_input("\nWhat is your name? ")
	vacation_poll = raw_input("If you could visit one place in the world, where would you go? ")
	# Store the responses in the dictionary
	responses[name_poll] = vacation_poll

	# Find out if anyone else is going to take the poll
	repeat = raw_input("Would another person like to take this poll? ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name_poll, vacation_poll in responses.items():
	print(name_poll + " would like to go to " + vacation_poll + ".")
