# 8-9 Magicians
def show_magicians(magician_names):
	"""Print a simple greeting to each magician"""
	for magician in magician_names:
		message = "My favorite magician, " + magician.title() + ", is amazing!"
		print(message)

magician_names = ['ken dog', 'kenneth', 'ken']
show_magicians(magician_names)