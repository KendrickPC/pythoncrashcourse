# Must use python3

filename = 'abigail.txt'

try:
	with open (filename) as file_object:
		contents = file_object.read()
except FileNotFoundError: 
	message = "The file you are trying to open, " + filename + ", \
does not exist."
	print(message)
else: 
	words = contents.split()
	number_of_words = len(words)
	print("The file, " + filename + ", has a total number of " + \
str(number_of_words) + " words in the file.")