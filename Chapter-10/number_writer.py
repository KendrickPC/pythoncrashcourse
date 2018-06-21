import json

numbers = [8, 23, 34, 99, 24, 12, 11, 30]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
