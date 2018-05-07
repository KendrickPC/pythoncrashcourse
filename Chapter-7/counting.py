# Introduction to While Loops

# The for loop takes a collection of items and executes a block of 
# code once for each item in the collection. In contrast, the while 
# loop runs as long as, or while, a certain condition is true.

# current_number = -3
# while current_number <= 5:
# 	print(current_number)
# 	current_number += 2



# Rather than breaking out of a loop entirely without executing the 
# rest of its code, you can use the continue statement to return to 
# the beginning of the loop based on the result of a conditional test.
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)