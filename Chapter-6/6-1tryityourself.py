# 6-1 Person

person = {
	'first_name': 'Kenderson',
	'last_name': 'Chang',
	'age': 27, 
	'city': 'Taipei'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


# 6-2 Favorite Number
favorite_number = {
	'joe': 8,
	'william': 7,
	'john': 2,
	'nancy': 88,
	'chloe': 50
}

number_joe = favorite_number['joe']
number_william = favorite_number['william']
number_john = favorite_number['john']
number_nancy = favorite_number['nancy']
number_chloe = favorite_number['chloe']

print("\nJoe's favorite number is " + str(number_joe) + ".")
print("William's favorite number is " + str(number_william) + ".")
print("John's favorite number is "  + str(number_john) + ".")
print("Nancy's favorite number is " + str(number_nancy) + ".")
print("Chloe's favorite number is " + str(number_chloe) + ".")

# 6-3 Glossary

glossary = {
	'for_loops': 'when you have a block of code which you want to \
repeat a fixed number of times.',
	'lists': 'a data structure in Python that is a mutable, \
or changeable, ordered sequence of elements.', 
	'dictionaries': 'mapping of unique keys to \
values. Dictionaries are mutable, which means they can be changed. The \
values that the keys point to can be any Python value.',
	'tuples': 'A tuple is a sequence of immutable Python objects.',
}

for_loops = glossary['for_loops']
lists = glossary['lists']
dictionaries = glossary['dictionaries']
tuples = glossary['tuples']

print("\nFor loops are traditionally used " + str(for_loops))
print("\nA list is " + str(lists))
print("\nA python dictionary is a " + str(dictionaries))
print("\n" + str(tuples))
