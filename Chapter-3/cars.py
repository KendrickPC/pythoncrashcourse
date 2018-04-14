# Sorting a List Permanently using the sort() Method

# sort() function permanantly changes the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# sorted() function does not permanantly change the order of the list

# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# The reverse() method changes the order of a list permanently, 
# but you can revert to the original order anytime by applying 
# reverse() to the same list a second time.

# print(cars)
# cars.reverse()
# print(cars)
# cars.reverse()
# print(cars)

# Finding the Length of a List
# Python counts the items in a list starting with one, so
# you shouldn't run into any off by one errors when
# determining the length of a list.
message = "\nThe amount of cars in the cars list is "
print(message)  
print(len(cars))

