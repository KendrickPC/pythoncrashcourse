# Must use python3
# Saving and Reading User-Generated Data

import json

username = input("What is your name? ")

# Creating username.json file
filename = 'username.json'
# Consider using append over write
with open(filename, 'a') as file_object:
    json.dump(username, file_object)
    print("We will remember your username when you come back, " +
          username + ".")
