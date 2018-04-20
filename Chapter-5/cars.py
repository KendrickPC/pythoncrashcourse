cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


# checking for equality
# Terminal Python editor

# Testing for equality is case sensitive in Python.
# == is a check sign for true or false

car1 = 'bmw'
print(car1 == 'bmw')

car2 = 'audi'
print(car2 == 'bmw')

# Ignoring case when checking
car3 = 'Audi'
print(car3 == 'audi')
print(car3.lower() == 'audi')