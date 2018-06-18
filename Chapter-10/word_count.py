# Must use python3
def count_words(filename):
	''' Count the number of words in a file. '''
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		message = "Sorry, the file " + filename + " does not exist."
		print(message)
	else: 
		# Count the number of words in a file.
		words = contents.split()
		number_of_words = len(words)
		print("The file " + filename + " has " + str(number_of_words) + \
" number of words.")

filenames = ['abigail.txt', 'book_1.txt', 'book_2.txt', 
'book_3.txt']

''' Loop through all files to count the number of words for each document '''
for filename in filenames:
	count_words(filename)
