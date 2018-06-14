# Opens and reads txt files

# Windows systems will sometimes interpret forward slashes in file paths
# correctly. If you are using Windows and you are not getting the results you
# expect, make sure you try using backslashes.


with open('Chapter-10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
