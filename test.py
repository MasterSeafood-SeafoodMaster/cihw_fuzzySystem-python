import Car_toolkit as ct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import matplotlib.animation as animation
fig, ax = plt.subplots()
square, car_pos, endline = ct.getSquare("軌道座標點.txt")
frame=0
while (not(ct.inBox(car_pos[0], car_pos[1])))and frame<50:
	
	plt.xlim([-20, 50])
	plt.ylim([-10, 60])
	sX = square[:, 0]; sY = square[:, 1]
	plt.plot(sX, sY)
	rect = Rectangle((18, 37), 12, 3, linewidth=1, edgecolor='r', facecolor='none')
	circle = Circle((car_pos[0], car_pos[1]), 3, fill=False)

	sensors, min_ds, min_ds_point = ct.draw_sensors(car_pos[0], car_pos[1], car_pos[2], square)
	rs, fs, ls = sensors
	rd, fd, ld = min_ds
	rp, fp, lp = min_ds_point
	
	theta=0
	if rd<10:
		theta=0
	elif fd<10:
		theta=40
	elif ld<10:
		theta=0

	ax.plot([car_pos[0], fs[0]], [car_pos[1], fs[1]], 'r-', linewidth=2)
	ax.plot([car_pos[0], ls[0]], [car_pos[1], ls[1]], 'g-', linewidth=2)
	ax.plot([car_pos[0], rs[0]], [car_pos[1], rs[1]], 'b-', linewidth=2)

	for i in range(3):
		sp = np.array(min_ds_point[i])
		plt.scatter(sp[0], sp[1])
		plt.annotate(str(round(min_ds[i], 2)), xy=(sp[0], sp[1]), xytext=(sp[0]+0.1, sp[1]+0.1))

	ax.add_artist(circle)
	ax.add_artist(rect)
	car_pos = ct.nextPos(car_pos[0], car_pos[1], car_pos[2], theta)
	
	file_name="./index/"+str(frame)+".png"
	fig.savefig(file_name)
	print(file_name, "saved")
	ax.cla()
	frame += 1

from PIL import Image
import os

print("saving gif")
folder_path = "./index"
image_list = []
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        number = int(filename.split(".")[0])
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)
        image_list.append((number, image))

image_list.sort(key=lambda x: x[0])
sorted_images = [img for _, img in image_list]

save_path = "./animation.gif"
sorted_images[0].save(save_path, save_all=True, append_images=sorted_images[1:], duration=100, loop=0)
