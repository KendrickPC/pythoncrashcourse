# 8-12 Sandwiches:

def make_sandwiches(*ingredients):
	"""Print a list of ingredients the sandwiches need"""
	print("\nMaking sandwich:")
	for ingredient in ingredients:
		print("\tAdding " + ingredient + " to your sandwich.")
	print("Your sandwich is ready.")

make_sandwiches('bread')
make_sandwiches('meat', 'lettuce')
make_sandwiches('tomatoes', 'pickles', 'mayo')