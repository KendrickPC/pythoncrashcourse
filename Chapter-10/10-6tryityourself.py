# 10-6. Addition: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert the
# input to an int, you will get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError
# if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text
# instead of a number.

# python 3 gives a ValueError
# python 2.7 gives a NameError

# Except block will route for python 3 ValueError

try:
    prompt_1 = input("Please add a number: ")
    prompt_1 = int(prompt_1)

    prompt_2 = input("Please give me another number: ")
    prompt_2 = int(prompt_2)

except ValueError:
    print("Please input a real number buddy.")

else:
    sum = prompt_1 + prompt_2
    print("The sum of " + str(prompt_1) + " and " + str(prompt_2) + " equals " + str(sum) + ".")
