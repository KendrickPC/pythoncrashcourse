# Passing Arguments
def describe_pet(animal_type, pet_name):
	"""display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'dog', pet_name = 'abigail')
describe_pet(animal_type = 'dog', pet_name = 'perkins')
describe_pet('cat', 'ding ding')

# order matters in positional arguments

# When you use keyword arguments, be sure to use the exact 
# names of the parameters in the functions definition.

