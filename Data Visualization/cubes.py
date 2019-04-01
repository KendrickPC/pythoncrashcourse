# import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 75]

# plt.scatter(x_values, y_values, linewidth=5)

# plt.show()

import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=40)

plt.axis([0, 5000, 0, 125000000000])

plt.show()
