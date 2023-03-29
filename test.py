import Car_toolkit as ct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

square, car_pos, endline = ct.getSquare("軌道座標點.txt")

while not(ct.inBox(car_pos[0], car_pos[1])):
	fig, ax = plt.subplots()
	plt.xlim([-20, 50])
	plt.ylim([-10, 60])
	sX = square[:, 0]; sY = square[:, 1]
	plt.plot(sX, sY)
	rect = Rectangle((18, 37), 12, 3, linewidth=1, edgecolor='r', facecolor='none')
	circle = Circle((car_pos[0], car_pos[1]), 3, fill=False)

	fs, ls, rs, fd, ld, rd = ct.draw_sensors(car_pos[0], car_pos[1], car_pos[2], square)

	ax.plot([car_pos[0], fs[0]], [car_pos[1], fs[1]], 'r-', linewidth=2)
	ax.plot([car_pos[0], ls[0]], [car_pos[1], ls[1]], 'g-', linewidth=2)
	ax.plot([car_pos[0], rs[0]], [car_pos[1], rs[1]], 'b-', linewidth=2)

	ax.add_artist(circle)
	ax.add_artist(rect)
	plt.show()


	car_pos = ct.nextPos(car_pos[0], car_pos[1], car_pos[2], 0)
	#print("fd", fd)
	#print("ld", ld)
	#print("rd", rd)

