# Must use python3

# Million digits of pi found in the following link. Copy and paste.
# http://www.eveandersson.com/pi/digits/1000000

# When Python reads from a text file, it interprets all text in the file as
# a string. If you read in a number and want to work with that value in a
# numerical context, you will have to convert it to an integer using the int()
# function or convert it to a float using the float() function.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:] + "...")
print(len(pi_string))

# Is your birthday contained in pi?
birthday = input("Enter your birthday in the form of mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
