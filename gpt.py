import math
import numpy as np
import matplotlib.pyplot as plt

def draw_sensors(x, y, angle, walls):
    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Plot the walls
    ax.plot(walls[:, 0], walls[:, 1], 'k-', linewidth=2)

    # Calculate the positions of the three sensors
    front_sensor = np.array([x, y]) + 50 * np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle))])
    left_sensor = np.array([x, y]) + 50 * np.array([math.cos(math.radians(angle + 45)), math.sin(math.radians(angle + 45))])
    right_sensor = np.array([x, y]) + 50 * np.array([math.cos(math.radians(angle - 45)), math.sin(math.radians(angle - 45))])

    # Plot the sensors
    ax.plot([x, front_sensor[0]], [y, front_sensor[1]], 'r-', linewidth=2)
    ax.plot([x, left_sensor[0]], [y, left_sensor[1]], 'g-', linewidth=2)
    ax.plot([x, right_sensor[0]], [y, right_sensor[1]], 'b-', linewidth=2)

    # Calculate the distances from each sensor to the nearest wall
    front_distances = np.sqrt(np.sum((walls - front_sensor) ** 2, axis=1))
    left_distances = np.sqrt(np.sum((walls - left_sensor) ** 2, axis=1))
    right_distances = np.sqrt(np.sum((walls - right_sensor) ** 2, axis=1))

    plt.show()
    return front_distances.min(), left_distances.min(), right_distances.min()

import Car_toolkit as ct
square, car_pos, endline = ct.getSquare("軌道座標點.txt")
print(draw_sensors(car_pos[0], car_pos[1], car_pos[2], square))