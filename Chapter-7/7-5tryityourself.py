# 7-5 Movie Tickets

age = input("How old are you in human years? ")
age = int(age)

if age < 3:
	print("\nYour movie tickets are free!")
elif age <= 12:
	print("\nYour movie tickets are $10.00 USD.")
else:
	print("\nYour movie tickets are $15.00 USD.")