# 5-8 Hello Admin
usernames = ['antdoggy', 'kennethpchang', 'brotherkendrick', 'admin', 'skinnybones', 'kenderson']

for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + username + ", thank you for logging in.")

# 5-9 No Users
usernamesIfTest = []

if usernamesIfTest:
	for userNameTest1 in usernamesIfTest:
		print("\nAdding " + userNameTest1 + " .")
	print("\nFinished adding User Name.")
else:
	print("\nWe need to find some users!")

# Format for above code found below:
# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		print("Adding " + requested_topping + ".")
# 	print("\nFinished making your pizza.")
# else:
# 	print("Are you sure you want a plain pizza?")

# 5-10 Checking Usernames
current_users = ['barackObama', 'brownBear', 'cony', 'kendersonpc', 'xiJingPing']

new_users = ['candyLiu', 'playstation', 'xbox', 'windowsXP', 'kendersonpc']

# current_users_lower_case = []
# for user in current_users:
# 	current_users_lower_case.append(user.lower())

current_users_lower_case = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower_case:
		print("\nSorry buddy, " + new_user + " has been taken.")
	else:
		print("\nGreat choice buddy, " + new_user + " is still available")


# 5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else: 
		print(str(number) + "th")

# 5-12 Styling if statements:
	# Code is PEP8 compliant

# 5-13
	# Writing python code that can write code by itself (using large data sets. 




















