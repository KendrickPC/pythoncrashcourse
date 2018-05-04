 # Pets: Make several dictionaries, where the name of each dictionary is the name of a pet.
 # In each dictionary, include the kind of animal and the owners name. 
 # Store these dictionaries in a list called pets . Next, loop through your list and
 # as you do print everything you know about each pet.

# empty list called pets
pets = []

pet = {
	'animal_type': 'dog',
	'name': 'abigail',
	'sex': 'female',
	'breed': 'border collie',
	'owner': 'kenneth p chang',
}
pets.append(pet)

pet = {
	'animal_type': 'dog',
	'name': 'perkins',
	'sex': 'female',
	'breed': 'corgi',
	'owner': 'kenneth p chang',
}
pets.append(pet)

pet = {
	'animal_type': 'cat',
	'name': 'buddy',
	'sex': 'male',
	'breed': 'mixed',
	'owner': 'david son ngo',
}
pets.append(pet)

# Testing for breaks
# print(pets)

for pet in pets: 
	pet_info = pet['animal_type']
	master = pet['owner']
	pet_name = pet['name']
	pet_breed = pet['breed']
	pet_sex = pet['sex']

	print("The " + pet_info + "'s owner is " + master.title() + "." \
		+ " The " + pet_info + "'s " + "name is " + pet_name.title() + ". " \
		+ "The pet's breed is " + pet_breed + " and is a "+ pet_sex)



