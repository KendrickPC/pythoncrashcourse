# 4-10 Slices:
kensFavoriteBasketballPlayers = ['michael jordan', 'larry bird', 'magic johnson', 'kobe bryant', 'anfernee hardaway', "shaquille o'neal", 'lebron james', 'stephen curry', 'kevin durant', 'jeremy lin']

# print(kensFavoriteBasketballPlayers)
print("\nThe first three items in the list are:")
print(kensFavoriteBasketballPlayers[0:3])

print("\nThree items from the middle of the list are:")
print(kensFavoriteBasketballPlayers[3:6])

# LeBum is left off the list
print("\nThe last three items in the list are:")
print(kensFavoriteBasketballPlayers[-3:])

# 4-11 My Pizzas, Your Pizzas:
print("\nFavorite Foods List")
kens_foods = ['japanese', 'mexican', 'italian']
girlfriend_foods = kens_foods[:]

kens_foods.append('french')
girlfriend_foods.append('taiwanese')

print("\nKen's favorite foods are:")
print("kens_foods")
print("\nKen's girlfriend's favorite foods are:")
print(girlfriend_foods)

# 4-12 More Loops:
fruits = ['apple', 'oranges', 'grapes', 'pineapples']
for fruit in fruits[:]:
	print(fruit)

print("\nKen's favorite foods are:")
for foodie in kens_foods[:]:
	print(foodie)

girlfriend_foods.pop(2)
girlfriend_foods.pop(1)
girlfriend_foods.append('chinese')
girlfriend_foods.append('vietnamese')

print("\nCandy's favorite foods are:")
for yummies in girlfriend_foods[:]:
	print(yummies)