# 6-7 People:
people = []

person = {
	'first_name': 'kenderson',
	'last_name': 'chang',
	'age': 27, 
	'city': 'taipei city',
	'username': 'kendrickpc',
	}

people.append(person)

person = {
	'first_name': 'brown',
	'last_name': 'bear',
	'age': 8,
	'city': 'taipei city',
	'username': 'brownbear',
}

people.append(person)

person = {
	'first_name': 'cony',
	'last_name': 'rabbit',
	'age': 8,
	'city': 'taipei city',
	'username': 'conyrabbit',
}

people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    usernameID = person['username']
	# print statement is inside the for loop    
    print(name + ", of " + city + ", is " + age + " years old." + " Their username is: " + usernameID)

