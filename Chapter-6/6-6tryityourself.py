# 6-4 Glossary 2

glossary = {
	'for loops': 'When you have a block of code which you want to \
repeat a fixed number of times.',
	'lists' : 'A data structure in Python that is a mutable, \
or changeable, ordered sequence of elements.', 
	'dictionaries' : 'Mapping of unique keys to \
values. Dictionaries are mutable, which means they can be changed. The \
values that the keys point to can be any Python value.',
	'tuples' : 'A tuple is a sequence of immutable Python objects.',
	'attribute' : 'Values associated with an individual object. \
Attributes are accessed using the dot syntax, a.x means fetch the \
x attribute from the a object.',
	'nested scope' : 'The ability to refer to a variable in an enclosing \
definition. For instance, a function defined inside another function can \
refer to variables in the outer function. Note that nested scopes work only \
for reference and not for assignment which will always write to the innermost \
scope. In contrast, local variables both read and write in the innermost scope. \
Likewise, global variables read and write to the global namespace.',
	'object oriented' : 'Programming typified by a data-centered (as opposed to \
a function-centered) approach to program design.',
	'strings' : 'One of the basic types in Python that store text. In Python 2.X \
strings store text as a string of bytes, and so the string type can also be used \
to store binary data. Also see Unicode.',
	'mapping' : 'A container object (such as dict) that supports arbitrary key \
lookups using __getitem__.',
}
print("Python Vocabulary Words:")
for vocabulary, definitions in glossary.items():
	print("\n" + vocabulary.title() + " : " + definitions)

# 6-5 Rivers
rivers = {
	'nile' : 'egypt',
	'amazon' : 'brazil',
	'yangtze' : 'china',
}

print("\nRiver Dictionary Pairs:")
for river, country in rivers.items():
	print("The " + river.title() + " river runs through the country of "
+ country.title() + ".")

print("\nThe following rivers are available in the data set:")
for river in rivers.keys():
	print(" - " + river.title())

print("\nThe following countries are available in the data set:")
for country in rivers.values():
	print(" - " + country.title())

# 6-6 Polling
# print("\nPolling:")
# for names in favorite_languages.keys():
# 	print("Thank you " + names.title() + " for taking our poll.")

# unpolled = {
# 	'jackson': '',
# 	'wesley': '',
# 	'michael': '',
# }

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

# for new_names in unpolled.keys():
# 	print("Hello " + new_names.title() + ", would you please take our poll?")
print("\nCoding Poll:")
coders = ['jackson', 'wesley', 'john', 'jen', 'edward', 'hamilton', 'william', 'phil']

for coder in coders:
	if coder in favorite_languages.keys():
		print("Thank you " + coder.title() + " for taking Ken Doggy's poll.")
	else:
		print("Hello " + coder.title() + ", what's your favorite coding language?")
