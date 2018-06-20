# Must use python3
def count_words(filename):
	''' Count the number of words in a file. '''
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		# message = "Sorry, the file " + filename + " does not exist."
		# print(message)
		pass
	else: 
		# Count the number of words in a file.
		words = contents.split()
		number_of_words = len(words)
		print("The file " + filename + " has " + str(number_of_words) + \
" number of words.")

filenames = ['prince_and_the_pauper.txt', 'huckleberry_finn.txt'
, 'tom_sawyer.txt', 'great_expectations.txt', 'python.txt']

''' Loop through all files to count the number of words for each document '''
for filename in filenames:
	count_words(filename)
