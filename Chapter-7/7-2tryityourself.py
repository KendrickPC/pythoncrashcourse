# 7-2 Restaurant Seating

group_party = input("How many people are with your dinner group? ")
group_party = int(group_party)

if group_party > 8:
	print("Please wait to be seated.")
else: 
	print("Your table is ready now.")