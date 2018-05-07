# A modulo just tells you what the remainder is

# If you’re using Python 2.7, use raw_input() instead of input().

number = raw_input("Enter a number, and I'll tell if you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
# elif number != int(number):
# 	number = raw_input("Enter a number, and I'll tell if you if it's even or odd: ")
# 	number = int(number)
else:
	print("\nThe number " + str(number) + " is odd.")