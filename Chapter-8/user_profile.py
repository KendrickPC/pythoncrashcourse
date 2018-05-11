# The double asterisks before the parameter **user_info cause 
# Python to create an empty dictionary called user_info and 
# pack whatever name value pairs it receives into this dictionary.

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about the user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('kenneth', 'chang',
							location='taipei',
							field='computer science')
print(user_profile)