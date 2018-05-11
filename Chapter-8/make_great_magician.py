def show_magicians(magicians):
	"""Print a simple greeting to each magician"""
	for magician in magicians:
		print(magician)

def make_great(magicians): 
	"""Adding 'the great' to each magician's name."""
	# Building a new list to hold great magicians
	great_magicians = []
	# Make each magician great, and add it to great_magicians
	while magicians:
		magician = magicians.pop()
		great_magician = magician + ' the Great'
		great_magicians.append(great_magician)
	# Add the great magicians back into magician_names
	for great_magician in great_magicians:
		magicians.append(great_magician)

	return magicians