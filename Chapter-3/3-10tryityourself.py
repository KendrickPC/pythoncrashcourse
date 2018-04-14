# 3-8 Seeing the World: 
bucket_list_cities = ['sydney', 'sao paolo', 'buenos aires', 'mumbai', 'moscow']
print(bucket_list_cities)
print(sorted(bucket_list_cities))
print(bucket_list_cities)

bucket_list_cities.reverse()
print(bucket_list_cities)
bucket_list_cities.reverse()
print(bucket_list_cities)
bucket_list_cities.sort(reverse=True)
print(bucket_list_cities)

# 3-9 Dinner Guests
guest_list = ['Barack Obama', 'Xi Jing Ping', 'Stephen Curry']
print(len(guest_list))

#Every Function: 
languages = ['chinese', 'english', 'sign language', 'spanish', 'hindi', 'arabic', 'portuguese', 'russian']

# functions learned in Chapter 3 are as follows:
# title()
# append()
# insert()
# del listName[x]
# pop()
# remove()
# sort()
# sorted()
# reverse()
# len(listName)

print(languages[2]).title()
languages.append('german')
print(languages)
languages.insert(4, 'french')
print(languages)
del languages[2]
print(languages)
popped_off = languages.pop(0)
print(languages)
languages.remove('arabic')
print(languages)
# languages.sort()
# print(languages)

print(sorted(languages))
languages.reverse()
print(languages)
print(len(languages))
print(languages[-1])