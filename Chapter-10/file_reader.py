# Opens and reads txt files

# Windows systems will sometimes interpret forward slashes in file paths
# correctly. If you are using Windows and you are not getting the results you
# expect, make sure you try using backslashes.


filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string +=line.rstrip()

print(pi_string)
print(len(pi_string))