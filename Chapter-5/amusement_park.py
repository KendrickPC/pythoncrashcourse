# The if-elif-else Chain

age = 12

# if age < 4:
# 	print("Your admission is $0.00 USD")
# elif age < 18:
# 	print("Your admission is $5.00 USD")
# else:
# 	print("Your admission is $10.00 USD")

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5

print("Your admission cost is $" + str(price) + ".")

# Python does not require an else block at the end 
# of an if-elif chain.
# If you have a specific final condition you are testing for, 
# consider using a final elif block and omit the else block. 
# As a result, you will gain extra confidence that your code will 
# run only under the correct conditions.