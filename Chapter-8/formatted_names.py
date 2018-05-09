# def get_formatted_name(first_name, last_name):
# 	"""Return a full name, neatly formatted"""
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)

# Middle Name Problem
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted"""
	if middle_name:
		return first_name.title() + ' ' + middle_name.title() + ' ' + last_name.title()
	else:
		return first_name.title() + ' ' + last_name.title() 

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
musician = get_formatted_name('kenneth', 'chang', 'peng') 
print(musician)