# Defining a Tuple

# Sometimes you will want to create a list of items 
# that cannot change. Tuples allow you to do just 
# that. Python refers to values that cannot change 
# as immutable, and an immutable list is called a tuple.

dimensions = (200, 50)

# dimensions[0] = 300

# print(dimensions[0])
# print(dimensions[1])
print("Original Dimensions:")
for dimension in dimensions:
	print(dimension)

print("\nModified Dimensions:")
dimensions = (400, 100)
for dimension in dimensions:
	print(dimension)