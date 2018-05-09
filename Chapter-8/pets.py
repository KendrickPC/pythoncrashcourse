# Passing Arguments
# def describe_pet(animal_type, pet_name):
# 	"""display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type = 'dog', pet_name = 'abigail')
# describe_pet(animal_type = 'dog', pet_name = 'perkins')
# describe_pet('cat', 'ding ding')

# order matters in positional arguments

# When you use keyword arguments, be sure to use the exact 
# names of the parameters in the functions definition.

# Default Values
def describe_pet(pet_name, animal_type='dog'):
	"""display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('abigail')
describe_pet(pet_name='harry', animal_type='hamster')

# When you use default values, any parameter with a default value needs to 
# be listed after all the parameters that dont have default values. This 
# allows Python to continue interpreting positional arguments correctly.

 # A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')