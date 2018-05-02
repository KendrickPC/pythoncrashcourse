favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

# You should not nest lists and dictionaries too deeply. If you are 
# nesting items much deeper than what you see in the preceding examples
# or you are working with another code with significant levels 
# of nesting, most likely a simpler way to solve the problem exists.
