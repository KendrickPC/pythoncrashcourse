"""
15-7. Two D8s: Create a simulation showing what happens if you roll
two eight-sided dice 1000 times. Increase the number of rolls
gradually until you start to see the limits of your system’s
capabilities.
"""

# Slow down in processing begins at 1 million rolls in line 20.

import pygal

from die8 import Die


# Create two D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice X times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                 '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "frenquency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('testing.svg')

print(frequencies)
