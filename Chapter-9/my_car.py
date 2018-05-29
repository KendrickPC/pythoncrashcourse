# Has not been checked by PEP8 standardization
from car import Car


kens_new_car = Car('audi', 'a8', '2017')
print(kens_new_car.get_descriptive_name())

# car.py line 11 function __init__
# car.py line 20 calling under read_odometer
kens_new_car.odometer_reading = 23
# car.py calling line 18 function read_odometer
kens_new_car.read_odometer()
