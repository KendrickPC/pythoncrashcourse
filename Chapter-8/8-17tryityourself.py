"""
PEP8 Online Check
Check 3 programs to follow styling guides and pass with zero errors
http://pep8online.com/
"""


# 8-13 User Profile:
# The double asterisks before the parameter **user_info cause
# Python to create an empty dictionary called user_info and
# pack whatever name value pairs it receives into this dictionary.


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('kenneth', 'chang',
                             location='taipei',
                             sex='male',
                             favorite_drink='coffee',
                             field='computer science')
print(user_profile)


# 8-11 Unchanged Magicians:


def show_magicians(magicians):
    """Print a simple greeting to each magician"""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Adding 'the great' to each magician's name."""
    # Building a new list to hold great magicians
    great_magicians = []
    # Make each magician great, and add it to great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    # Add the great magicians back into magician_names
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Ken Dog', 'Kenneth', 'Ken']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)


# 8-14 Cars:


def make_car(brand, model_id, **options):
    """Dictionary representing a car."""
    car_dictionary = {
        'brand': brand,
        'model_id': model_id,
        }
    for option, option_value in options.items():
        car_dictionary[option] = option_value
    return car_dictionary

kens_first_car = make_car('toyota', 'camry', color='blue', year=1997)

kens_second_car = make_car('toyota', 'corolla', color='silver', year=2000)

kens_third_car = make_car('toyota', 'camry', color='silver', year=2003)

print(kens_first_car)
print(kens_second_car)
print(kens_third_car)
