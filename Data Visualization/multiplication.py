"""
15-9. Multiplication: When you roll two dice, you usually add the two
numbers together to get the result . Create a visualization that shows
what happens if you multiply these numbers instead.
"""

import pygal

from die import Die


# Create two D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides * die_2.num_sides
for value in range(1, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "The product results of rolling two D6 dice X times."
hist.x_labels = [str(x) for x in range(1, max_results+1)]
hist.x_title = "Result"
hist.y_title = "Frenquency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('D6_product_results.svg')

print(frequencies)
