# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to
# fail silently if either file is missing.

def cartoon_animal_names(filename):
    # Read the names of cartoon animals from a file
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        # error_message = "Sorry, the file name " + filename + " does not exist."
        # print(error_message)
    else:
        names = contents
        print(names.title())

filenames = ['cats.txt', 'dogs.txt', 'monkeys.txt', 'rabbits.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    cartoon_animal_names(filename)
