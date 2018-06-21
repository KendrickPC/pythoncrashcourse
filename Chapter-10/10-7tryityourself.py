# Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so
# the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

print("Enter 'q' to quit at any time.")

while True:
    try:
        prompt_1 = input("Please add a number: ")
        if prompt_1 == 'q':
            break
        prompt_1 = int(prompt_1)

        prompt_2 = input("Please give me another number: ")
        if prompt_2 == 'q':
            break
        prompt_2 = int(prompt_2)

    except ValueError:
        print("Please input a real number buddy.")

    else:
        sum = prompt_1 + prompt_2
        print("The sum of " + str(prompt_1) + " and " + str(prompt_2) + " equals " + str(sum) + ".")
