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
