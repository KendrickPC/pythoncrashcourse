# Favorite Places

# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, 
# and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to 
# name a few of their favorite places. Loop through the dictionary, 
# and print each persons name and their favorite places.

favorite_places = { 
	'kenderson': 'taiwan',
	'charles': 'guam',
	'peter': 'california',
	}

for name, favorite_place in favorite_places.items():
	print(name.title() + "'s favorite place in the whole world is " + favorite_place.title() + ".")


