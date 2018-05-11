# 8-10 Great Magicians:

# Start with a copy of your program from Exercise 8-9. 
# Write a function called make_great() that modifies the 
# list of magicians by adding the phrase the Great to 
# each magicians name. Call show_magicians() to see 
# that the list has actually been modified.

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

magicians = ['Ken Dog', 'Kenneth', 'Ken']
show_magicians(magicians)

print("\nGreat magicians:")
make_great(magicians)
show_magicians(magicians)
