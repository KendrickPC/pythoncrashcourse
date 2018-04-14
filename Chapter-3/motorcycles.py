# Changing, Adding, and Removing Elements
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# motorcycles[1] = 'kawasaki'
# motorcycles[2] = 'triumph'
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles)

# Inserting Elements into a List
# motorcycles = ['honda', 'yamaha', 'suzuki']

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the del Statement
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# # del motorcycles[0]
# del motorcycles[1]
# print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# pop vs del
# when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("\nThe " + too_expensive.title() + " is too expensive for me!")