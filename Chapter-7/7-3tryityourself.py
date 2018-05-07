# 7-3 Multiples of Ten

divisible_by_ten = raw_input("Please input a number that is divisible by ten: ")
divisible_by_ten = int(divisible_by_ten)

if divisible_by_ten % 10 == 0:
	print("\nThe number " + str(divisible_by_ten) + " is divisible by ten.")
else: 
	print("\nThe number " + str(divisible_by_ten) + " is not divisible by ten.")