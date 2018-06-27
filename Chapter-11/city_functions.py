# formatted_city_function stored in city_functions.py
def get_formatted_city(city, country, population=''):
    if population:
        full_city_info = city + ', ' + country + ' - ' + population
    else:
        full_city_info = city + ', ' + country
    return full_city_info.title()
