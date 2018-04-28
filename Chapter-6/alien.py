# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# To get the value associated with a key, give the name of the
# dictionary and then place the key inside a set of square brackets.

# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Notice that the order of the key-value pairs does not match the
# order in which we added them. Python does not care about the 
# order in which you store each key-value pair; it cares only about
# the connection between each key and its value.

# Starting With An Empty Dictionary
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# Modifying Values in a Dictionary

# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position' : 0, 'y_position': 25, 'speed': 'fast'}
print("Orginal x-position: " + str(alien_0['x_position']))

# Move alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
elif alien_0['speed'] == 'fast':
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
# alien_0['speed'] = fast

print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
