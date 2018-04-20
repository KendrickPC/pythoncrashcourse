# 5-1 try it yourself
nba_2018_champion = 'warriors'
print("Will the NBA 2018 Champions be the Golden State Warriors? I predict True.")
print(nba_2018_champion == 'warriors')

print("\nWill the NBA 2018 Champions be the Houston Rockets? I predict False.")
print(nba_2018_champion == 'rockets')


good_2018_NBA_teams = ['warriors', 'rockets', 'raptors', 'celtics', 'cavaliers']
# 5 tests evaluating to True
print("\nFive tests evaluating to True")
print('warriors' in good_2018_NBA_teams)
print('rockets' in good_2018_NBA_teams)
print('raptors' in good_2018_NBA_teams)
print('celtics' in good_2018_NBA_teams)
print('cavaliers' in good_2018_NBA_teams)

# 5 tests evaluating to False
print("\nFive tests evaluating to False")
print('blazers' in good_2018_NBA_teams)
print('nuggets' in good_2018_NBA_teams)
print('nets' in good_2018_NBA_teams)
print('lakers' in good_2018_NBA_teams)
print('knicks' in good_2018_NBA_teams)

# 5-2 try it yourself
# testing for equality with strings
print("\nTesting for equality with strings")
good_music = 'Coldplay'
print(good_music == 'Spice Girls')
# testing using the lower function
print("\nTesting using the lower function")
print(good_music.lower() == 'coldplay')
# Numerical Testing
print("\nNumerical Testing")
kens_age = 36
candys_age = 35
print(kens_age == 33)
print(candys_age != 38)
print(kens_age < 40)
print(kens_age > 20)
print(candys_age <= 30)
print(candys_age >= 40)

print("\nTesting for 'and' 'or' keyword")
print(kens_age > 40 and candys_age > 20)
print(kens_age > 40 or candys_age > 20)

watches = ['rolex', 'iwc', 'kenneth cole', 'casio']
print("\nTesting whether an item is in a list")
print('montblanc' in watches)
print("\nTesting whether an item is not in a list")
print('calvin klein' not in watches)