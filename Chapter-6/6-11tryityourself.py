# 6-11. Cities: Make a dictionary called cities . Use the names of three cities as keys in your dictionary . Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city . The keys for each citys dictionary should be something like country, population, and fact . Print the name of each city and all of the infor- mation you have stored about it .


# 6-11 Cities
cities = {
	'los angeles': {
		'country': 'united states',
		'population': 4000000,
		'fact': 'making movies',
	},
	'san francisco': {
		'country': 'united states',
		'population': 870000,
		'fact': 'rent being really expensive',
	},
	'cupertino': {
		'country': 'united states',
		'population': 60700,
		'fact': 'the hometown of kendrickpc'
	},
}

for city, city_information in cities.items():
	country_of_city = city_information['country']
	population_of_city = str(city_information['population'])
	fact_of_city = city_information['fact']
	print("\tThe city of " + city.title() + \
		", located in the country of the " + \
		country_of_city.title() + \
		", has a population of " + population_of_city \
		+ " and is known for " + fact_of_city + ".")
