favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
	print("\n" + name.title())

# Looping through the keys is actually the default behavior when looping through
# a dictionary, so

# for name in favorite_languages: = for name in favorite_languages.keys():

friends = ['phil', 'jen']

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " \
			+ favorite_languages[name].title() + "! Me too!")

if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")


# Looping Through a Dictionary Key in Order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking our poll.")

# Looping Through All Values in a Dictionary
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())