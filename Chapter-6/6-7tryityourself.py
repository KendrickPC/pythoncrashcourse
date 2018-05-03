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


for person in people:
	full_name = person['first_name'].title() + " " + person['last_name'].title() + "'s"
	
print(full_name)