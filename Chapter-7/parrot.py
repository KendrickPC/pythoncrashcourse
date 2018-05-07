# Raw input vs input
# https://stackoverflow.com/questions/5074225/python-unexpected-eof-while-parsing

# message = raw_input("Tell me something, and I will repeat it back to you: ")
# print("\t" + message)

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
# 	message = raw_input(prompt)

# 	if message != 'quit':
# 		print(message)


# Using a Flag variable active
active = True
while active:
	message = raw_input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)