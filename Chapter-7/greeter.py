# Input vs Raw Input

# https://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python3-x


# Add a space at the end of your prompts, after the colon, to separate the prompt from the user response, and to make it clear to your user where to enter their text.

# name = raw_input("Please enter your name: ")
# print("Hello, " + name + "!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = raw_input(prompt)

print("Hello, " + name + "!")

age = input("How old are you? ")
# age = int(age)

print(name + "'s age is " + age)
print(age >= 18)