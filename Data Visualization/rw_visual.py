import matplotlib.pyplot as plt

from refactoring import RandomWalk

"""
Generating multiple random walks. Keep making new walks,
as long as the program is active.
"""
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Reds, edgecolor='none', s=1)

    """
    The following code must be entered right before plt.show() so that the
    points are entered on top of the initial plot.
    """
    # Emphasize the first and last points.
    # Purple symbolizes first point.
    plt.scatter(0, 0, c='purple', edgecolors='none', s=100)
    # Yellow symbolizes last point.
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow',
                edgecolors='none', s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # If using python 2,7, use raw_input() instead of input().
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
