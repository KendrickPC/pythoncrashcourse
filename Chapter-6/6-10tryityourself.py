# 6-10. Favorite Numbers: Modify your program from 
# Exercise 6-2 (page 102) so each person can have more
# than one favorite number. Then print each persons 
# name along with their favorite numbers.


favorite_number = {
	'kobe': [8, 24],
	'jordan': [23, 6],
	'lebron': [23, 1],
}

for name , numbers in favorite_number.items():
	print(name.title() + "'s favorite numbers are:")
	for number in numbers:
		print(number)

