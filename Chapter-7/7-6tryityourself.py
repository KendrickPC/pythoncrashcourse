# 7-6 Three Exits

# Write different versions of either Exercise 7-4
# or Exercise 7-5 that do each of the following at least once:

# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "How old are you in human years?"
prompt += "\n(Enter 'quit' when you are finished): "

while True:
    age = raw_input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("\tYour movie ticket is free.")
    elif age <= 12:
        print("\tYour movie ticket is $10.00 USD.")
    else:
        print("\tYour movie ticket is $15.00 USD.")





