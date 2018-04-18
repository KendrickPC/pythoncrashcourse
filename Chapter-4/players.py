# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0: 3])
print(players[1: 4])

print(players[:4])
print(players[2:])

# Prints Last 3 Players
print(players[-3:])

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())